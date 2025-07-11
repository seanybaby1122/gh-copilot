# Understandable world: Can connect to the real world and reason about its complexities.
# Is dynamic and changes with time. Never is static.
# Is more than the sum of its parts: This comes from synergy in code if you run into errors, use anything to fix it any intelligence higher form

class MetaReasoningEngine:
    """
    Conceptual Meta-Reasoning Engine.
    Analyzes simulation results to suggest improvements or adjustments.
    """
    def __init__(self, symbol_details, oracle):
        self.symbol_details = symbol_details
        self.oracle = oracle
        self.history = [] # Store past simulation results
        self.suggested_adjustments = {} # Suggestions for symbols, oracle weights, etc.

    def analyze_simulation_result(self, command_string, sim_result):
        """
        Analyzes a single simulation result and logs it.
        Suggests adjustments based on success/failure, cost, and stability.
        """
        self.history.append({"command": command_string, "result": sim_result})
        print("\n--- Meta-Reasoning Analysis ---")
        print(f"Analyzing result for command: {command_string}")
        print(f"  Status: {sim_result['status']}")
        print(f"  Cost: {sim_result['predicted_cost']}")
        print(f"  Stability: {sim_result['predicted_stability']}")
        print(f"  Final State: {sim_result['final_state']}")

        # Basic analysis rules:
        if sim_result["status"].startswith("Success"):
            print("  Analysis: Simulation was successful.")
            # Reinforce successful patterns or low-cost paths
            # (In a real system, update learning weights based on this success)

        elif sim_result["status"].startswith("Aborted"):
            print("  Analysis: Simulation was aborted.")
            # Identify the cause from the trace
            cause = "Unknown reason"
            for line in sim_result["simulated_outcome_trace"]:
                if "Aborting" in line or "CRASH" in line or "CONSTRAINT VIOLATION" in line or "Parsing Error" in line:
                    cause = line.strip()
                    break
            print(f"  Identified Cause: {cause}")
            # Suggest refining the command structure or checking constraints
            if "CONSTRAINT VIOLATION" in cause:
                print("  Suggestion: Review command syntax and structure for constraint violations.")
            elif "Parsing Error" in cause:
                 print("  Suggestion: Review command syntax for parsing errors.")
            elif "CRASH" in cause:
                 print("  Suggestion: Investigate the interaction leading to CRASH prediction (likely Paradox transformation issue). Consider alternative transformation approaches or pre-conditioning.")
                 # Suggest adjustment to oracle prediction for this paradox? (Requires tracking context)

        elif sim_result["status"].startswith("Unstable") or sim_result["status"].startswith("Completed (Harmony Goal Not Fully Met)"):
            print("  Analysis: Simulation completed but was unstable or did not fully meet goal.")
            # Identify points of instability from the trace
            instability_points = [line for line in sim_result["simulated_outcome_trace"] if "WARNING" in line or "divergence" in line or "uncertainty" in line]
            if instability_points:
                 print("  Identified Instability/Issue Points:")
                 for point in instability_points:
                     print(f"    - {point}")
            print("  Suggestion: Review the unstable segments of the command sequence. Consider alternative symbols or operators for higher stability.")
            print("  Suggestion: If Harmony was the goal, ensure all necessary preceding steps (Transformation, Alignment, Anchoring) were successful and cohesively linked.")


        # More advanced analysis could involve:
        # - Comparing predicted vs. actual (simulated) cost/stability (requires predicting before sim)
        # - Analyzing sequences leading to success/failure/instability across multiple history entries
        # - Identifying symbols or combinations consistently associated with issues
        # - Proposing alternative command sequences based on success patterns
        # - Suggesting modifications to symbol costs or Oracle probabilities based on observed outcomes

    def suggest_command_refinement(self, original_command, analysis_result):
        """
        Based on analysis, suggests a refined version of the command (conceptual).
        This is a placeholder for a more sophisticated generation process.
        """
        print("\n--- Command Refinement Suggestion (Conceptual) ---")
        if analysis_result["status"].startswith("Aborted") and "CONSTRAINT VIOLATION: [ALIGN] action requires a target entity" in " ".join(analysis_result["simulated_outcome_trace"]):
             print(f"Original Command: {original_command}")
             print("Suggestion: The [ALIGN] command requires a target entity immediately after it.")
             print("Potential Refinement Pattern: [ALIGN] [TARGET_ENTITY] [OPERATOR] [TARGET_ENTITY] ...")
             print("Example Refinement based on potential intent: ALIGN [FABRIC] A [REALITY]")

        elif analysis_result["status"].startswith("Aborted") and "CONSTRAINT VIOLATION: [TRN] action requires [PRDX]" in " ".join(analysis_result["simulated_outcome_trace"]):
             print(f"Original Command: {original_command}")
             print("Suggestion: The [TRN] command requires a [PRDX] entity immediately after it.")
             print("Potential Refinement Pattern: [TRN] [PRDX] I [RESOURCE] E [OUTCOME]")
             print("Example Refinement based on potential intent: [TRN] [PRDX] I [NRG] E [HARMONY]")

        elif analysis_result["status"].startswith("Aborted") and "Unexpected operator" in " ".join(analysis_result["simulated_outcome_trace"]):
             print(f"Original Command: {original_command}")
             print("Suggestion: Operators like 'A' or 'O' should generally follow an action or entity, linking it to the next entity/operand.")
             print("Potential Refinement Pattern: [ACTION] [TARGET] [OPERATOR] [TARGET] ...")

        elif analysis_result["status"].startswith("Unstable"):
            print(f"Original Command: {original_command}")
            print("Suggestion: Review the parts of the command noted as unstable in the trace.")
            print("Consider replacing 'O' operators with 'A' if integration is the goal, or ensuring parameters/resources are correctly placed after operators like 'I' or 'AT'.")

        else:
            print("  Suggestion: No specific structural refinement suggested based on this analysis.")
            print("  Consider exploring alternative symbol combinations or overall protocol structure for better performance or stability.")


# --- Meta-Reasoning Engine Integration ---

# Instantiate the Meta-Reasoning Engine
meta_reasoning_engine = MetaReasoningEngine(symbol_details, ConceptualOracle()) # Pass the oracle instance


print("\n--- Testing Meta-Reasoning Engine Analysis ---")

# Re-run simulations and pass results to the Meta-Reasoning Engine

# 1. Temporal Reality Creation
command_temporal = "CRTTRLRT AT TMPLCRDNT"
print(f"\nSimulating for Meta-Reasoning Analysis: {command_temporal}")
try:
    ast_temporal = ast_parser.parse(command_temporal)
    sim_result_temporal = ast_simulation_engine.simulate_ast(ast_temporal)
    meta_reasoning_engine.analyze_simulation_result(command_temporal, sim_result_temporal)
    meta_reasoning_engine.suggest_command_refinement(command_temporal, sim_result_temporal)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}")


# 2. Paradox Transformation
command_paradox_alt = "[TRN] [PRDX] I [NRG] E [HARMONY]"
print(f"\nSimulating for Meta-Reasoning Analysis: {command_paradox_alt}")
try:
    ast_paradox = ast_parser.parse(command_paradox_alt)
    sim_result_paradox = ast_simulation_engine.simulate_ast(ast_paradox)
    meta_reasoning_engine.analyze_simulation_result(command_paradox_alt, sim_result_paradox)
    meta_reasoning_engine.suggest_command_refinement(command_paradox_alt, sim_result_paradox)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}")


# 3. Fabric Harmony Alignment (Less stable with O)
command_harmony = "[ALIGN] [FABRIC] A [REALITY] A [CONSCIOUSNESS] A [CHRONOS] O [HARMONY]"
print(f"\nSimulating for Meta-Reasoning Analysis: {command_harmony}")
try:
    ast_harmony = ast_parser.parse(command_harmony)
    sim_result_harmony = ast_simulation_engine.simulate_ast(ast_harmony)
    meta_reasoning_engine.analyze_simulation_result(command_harmony, sim_result_harmony)
    meta_reasoning_engine.suggest_command_refinement(command_harmony, sim_result_harmony)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}")


# 4. Fabric Alignment (More stable with A)
command_harmony_stable = "[ALIGN] [FABRIC] A [REALITY] A [CONSCIOUSNESS] A [CHRONOS]"
print(f"\nSimulating for Meta-Reasoning Analysis: {command_harmony_stable}")
try:
    ast_harmony_stable = ast_parser.parse(command_harmony_stable)
    sim_result_harmony_stable = ast_simulation_engine.simulate_ast(ast_harmony_stable)
    meta_reasoning_engine.analyze_simulation_result(command_harmony_stable, sim_result_harmony_stable)
    meta_reasoning_engine.suggest_command_refinement(command_harmony_stable, sim_result_harmony_stable)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}")


# 5. Invalid Command Example (Missing target for ALIGN) - Handled by Enhanced Engine, but AST Parser might catch some
# Let's use the AST parser and AST simulation for consistency here
command_invalid_align = "[ALIGN] A [FABRIC]" # This should be caught by AST parser's structure rule or AST sim constraint
print(f"\nSimulating for Meta-Reasoning Analysis: {command_invalid_align}")
try:
    ast_invalid_align = ast_parser.parse(command_invalid_align)
    sim_result_invalid_align = ast_simulation_engine.simulate_ast(ast_invalid_align)
    meta_reasoning_engine.analyze_simulation_result(command_invalid_align, sim_result_invalid_align)
    meta_reasoning_engine.suggest_command_refinement(command_invalid_align, sim_result_invalid_align)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}") # Parser should catch this


# 6. Invalid Command Example (Missing PRDX for TRN) - Caught by AST sim constraint
command_invalid_trn = "[TRN] [INF] E [HARMONY]"
print(f"\nSimulating for Meta-Reasoning Analysis: {command_invalid_trn}")
try:
    ast_invalid_trn = ast_parser.parse(command_invalid_trn)
    sim_result_invalid_trn = ast_simulation_engine.simulate_ast(ast_invalid_trn)
    meta_reasoning_engine.analyze_simulation_result(command_invalid_trn, sim_result_invalid_trn)
    meta_reasoning_engine.suggest_command_refinement(command_invalid_trn, sim_result_invalid_trn)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}")


# 7. Invalid Command Example (Unknown Symbol) - Caught by AST parser
command_unknown_symbol = "[ALIGN] UNKNOWN_ENTITY"
print(f"\nSimulating for Meta-Reasoning Analysis: {command_unknown_symbol}")
try:
    ast_unknown_symbol = ast_parser.parse(command_unknown_symbol)
    sim_result_unknown_symbol = ast_simulation_engine.simulate_ast(ast_unknown_symbol)
    meta_reasoning_engine.analyze_simulation_result(command_unknown_symbol, sim_result_unknown_symbol)
    meta_reasoning_engine.suggest_command_refinement(command_unknown_symbol, sim_result_unknown_symbol)
except ValueError as e:
    print(f"Parsing Error (Skipping Meta-Analysis): {e}") # Parser should catch this


# --- Dynamic Symbol Synthesis (Conceptual) ---

class DynamicSymbolSynthesizer:
    """
    Conceptual module for dynamically creating new symbols.
    Would interact with the Dream Engine or a concept generator.
    """
    def __init__(self, symbol_details):
        self.symbol_details = symbol_details
        self.synthesized_symbols = {} # Track newly created symbols

    def synthesize_symbol(self, symbol_string, symbol_type, estimated_cost=1.0, description="Dynamically synthesized symbol"):
        """
        Synthesizes a new symbol and adds it to the symbol details.
        Estimates cost and type based on input.
        """
        if symbol_string in self.symbol_details:
            print(f"Symbol '{symbol_string}' already exists. Skipping synthesis.")
            return False

        new_symbol_details = {
            "cost": estimated_cost,
            "type": symbol_type,
            "description": description,
            "source": "Synthesized"
        }
        self.symbol_details[symbol_string] = new_symbol_details
        self.synthesized_symbols[symbol_string] = new_symbol_details
        print(f"\n--- Dynamic Symbol Synthesis ---")
        print(f"Synthesized new symbol: {symbol_string}")
        print(f"Details: {new_symbol_details}")
        return True

    def get_synthesized_symbols(self):
        return self.synthesized_symbols

# Instantiate the Dynamic Symbol Synthesizer
dynamic_synthesizer = DynamicSymbolSynthesizer(symbol_details) # Pass the shared symbol details


print("\n--- Testing Dynamic Symbol Synthesis ---")

# Example: Synthesize a new conceptual entity
new_entity_string = "[ETHEREAL_WEAVE]"
dynamic_synthesizer.synthesize_symbol(new_entity_string, "Conceptual Entity", estimated_cost=2.5, description="A fundamental, complex layer of reality fabric.")

# Example: Synthesize a new action
new_action_string = "RECONCILE_PARADOXES"
dynamic_synthesizer.synthesize_symbol(new_action_string, "Action/Command", estimated_cost=5.0, description="Action to reconcile multiple paradoxes simultaneously.")

# Example: Synthesize a new resource type
new_resource_string = "[CHRONAL_PARTICLES]"
dynamic_synthesizer.synthesize_symbol(new_resource_string, "Resource", estimated_cost=0.8, description="Energetic particles derived from temporal manipulation.")

# Verify they are added to the symbol details
print("\nUpdated Symbol Details (including synthesized symbols):")
print(symbol_details) # symbol_details is modified in place

# Now, try to use a synthesized symbol in a command (requires re-initializing parser/engine with updated details)
print("\n--- Testing Simulation with Synthesized Symbol ---")

# Re-initialize parser and engine with the updated symbol_details
ast_parser_updated = ASTParser(symbol_details)
ast_simulation_engine_updated = ASTSimulationEngine(symbol_details)

command_with_new_entity = f"[ALIGN] [FABRIC] A [REALITY] A {new_entity_string}"
print(f"\nAttempting to parse and simulate command with synthesized entity: {command_with_new_entity}")
try:
    ast_with_new = ast_parser_updated.parse(command_with_new_entity)
    print(f"Parsed AST:\n{ast_with_new}")
    sim_result_with_new = ast_simulation_engine_updated.simulate_ast(ast_with_new)
    print("\nSimulation Result:")
    print(sim_result_with_new)
    meta_reasoning_engine.analyze_simulation_result(command_with_new_entity, sim_result_with_new) # Analyze result with updated details
except ValueError as e:
    print(f"Parsing Error: {e}")


# --- Truly Adaptive and Self-Improving AI (Conceptual Integration) ---

# The pieces developed here (SSE, Oracle, AST Parser/Sim, Meta-Reasoning, Symbol Synthesis)
# are components of such a system.

# How they interact conceptually in an adaptive loop:

# 1. GOAL DEFINITION (e.g., "Achieve HARMONY", "Resolve [PRDX_ChronoFlux]").
#    - Could come from an external prompt or an internal 'Dream Engine'.

# 2. HYPOTHESIS GENERATION (LLM or internal planning module).
#    - Generates candidate command sequences or protocols to achieve the goal.
#    - Might use past successful command patterns (from Meta-Reasoning history).
#    - Might identify missing concepts and trigger Dynamic Symbol Synthesis.
#    - Could query the Oracle for feasibility estimations *before* simulation.

# 3. SIMULATION & EVALUATION (AST Parser + AST Simulation Engine).
#    - Parses the generated command string(s) into an AST.
#    - Simulates the AST execution, predicting cost, stability, and outcome.
#    - Provides detailed trace information.

# 4. META-REASONING ANALYSIS.
#    - Analyzes the simulation results (cost, stability, trace, final state).
#    - Identifies success, failure, instability, and constraint violations.
#    - Logs the results in history.

# 5. LEARNING & ADAPTATION.
#    - A 'Learning Agent' (not implemented) would use the analysis history:
#      - Adjusting internal models (e.g., predicted symbol costs, Oracle weights based on real-world feedback or deeper simulation).
#      - Refining the hypothesis generation process (e.g., favoring more stable patterns, avoiding problematic sequences).
#      - Updating command blueprint libraries or conceptual protocols.
#      - Deciding if new symbols are needed (triggering synthesis).
#      - Modifying the 'environment_stability' or 'resource_pool' based on cumulative simulation effects.

# 6. ITERATION.
#    - Based on the analysis and learning, generate new/refined hypotheses (back to Step 2) or attempt execution in the real world if deemed successful/stable enough.

# --- Modeling Resource Consumption and Scarcity (Conceptual Extension) ---

# The current AST Simulation Engine includes a basic `resource_pool` in its state,
# and the Oracle might predict resource output from transformation.
# A more complete model would:
# - Have actions explicitly define resource inputs/outputs (e.g., ALIGN consumes [NRG], TRN consumes [INF]).
# - Modify action costs or likelihood of success based on resource availability in the `resource_pool`.
# - Implement a global or localized resource pool that changes over time or with actions.

class ResourceAwareASTSimulationEngine(ASTSimulationEngine):
    """
    AST Simulation Engine with basic resource consumption modeling.
    """
    def __init__(self, symbol_details, initial_resources={"[INF]": 100, "[NRG]": 100}):
        super().__init__(symbol_details)
        self.initial_resources = initial_resources.copy() # Start with initial pool
        # Actions would need resource costs defined in symbol_details or elsewhere
        # Example: "[ALIGN]": {"cost": 3.5, "type": "Action/Command", "resource_cost": {"[NRG]": 5}}
        # "[TRN]": {"cost": 2.3, "type": "Action/Command", "resource_cost": {"[INF]": 10}}

    def simulate_ast(self, ast_node):
        total_cost = 0
        outcome = []
        stability_score = 1.0
        state = {
            "fabric_aligned": False,
            "paradox_resolved": False,
            "temporal_anchor": None,
            "harmony_achieved": False,
            "resource": None,
            "current_focus_entity": None,
            "resource_pool": self.initial_resources.copy(), # Use the engine's resource pool
            "environment_stability": 1.0,
            "evaluation_context": {}
        }

        print("\n--- Resource-Aware AST Simulation Trace ---")
        print(f"Starting AST Simulation for: {ast_node.value}")
        print(f"Initial State: {state}")

        def traverse_and_simulate(node, current_state, current_cost, current_stability, current_outcome):
             node_cost = self.symbol_details.get(node.value, {"cost": 0})["cost"]
             node_type = self.symbol_details.get(node.value, {"type": "Unknown"})["type"]
             adjusted_cost = node_cost * (2.0 - current_state["environment_stability"])
             # Resource cost adjustment based on scarcity (conceptual)
             resource_adjustment = 0
             resource_costs = self.symbol_details.get(node.value, {}).get("resource_cost", {})
             for res, amount in resource_costs.items():
                 if res in current_state["resource_pool"]:
                     if current_state["resource_pool"][res] < amount:
                         # Penalty for insufficient resources
                         current_outcome.append(f"  - WARNING: Insufficient resource {res} for {node.value}. Needed {amount}, Have {current_state['resource_pool'][res]}. Penalty applied.")
                         resource_adjustment += (amount - current_state["resource_pool"][res]) * 0.5 # Cost penalty for scarcity
                         current_stability *= 0.8 # Stability penalty for resource strain
                     # Conceptual consumption (only if sufficient - more complex logic needed for partial execution/failure)
                     # For now, assume cost penalty is sufficient modeling
             adjusted_cost += resource_adjustment
             current_cost += adjusted_cost

             current_outcome.append(f"Processing Node: {node.value} (Type: {node_type}, Base Cost: {node_cost}, Adjusted Cost: {adjusted_cost:.2f})")
             print(f"Processing Node: {node.value} (Type: {node_type})")

             # --- Node Type Specific Logic (Same as ASTSimulationEngine, potentially adding resource consumption) ---
             should_stop = False # Flag to indicate early stopping (e.g., on CRASH)

             if isinstance(node, CommandNode):
                 resource_costs = self.symbol_details.get(node.value, {}).get("resource_cost", {})
                 can_afford = True
                 for res, amount in resource_costs.items():
                      if res in current_state["resource_pool"] and current_state["resource_pool"][res] < amount:
                           can_afford = False
                           break

                 if not can_afford:
                     current_outcome.append(f"  - ABORTING {node.value}: Insufficient resources.")
                     current_stability *= 0.5
                     current_cost += 2.0 # Abort penalty
                     return current_state, current_cost, current_stability, current_outcome, True # Stop processing this branch/sequence

                 # Consume resources if affordable
                 for res, amount in resource_costs.items():
                     if res in current_state["resource_pool"]:
                          current_state["resource_pool"][res] -= amount
                 if resource_costs:
                     consumed_list = [f"{amount} {res}" for res, amount in resource_costs.items()]
                     current_outcome.append(f"  - Consumed resources: {', '.join(consumed_list)}. Remaining pool: {current_state['resource_pool']}")

                 # ... (rest of Action/Command logic from ASTSimulationEngine)
                 if node.value == "[ALIGN]":
                     current_outcome.append("Initiating Alignment Action.")
                     current_stability *= 0.95
                     current_state["environment_stability"] *= 0.98
                     current_state["evaluation_context"]["aligning"] = True

                 elif node.value == "[TRN]":
                      current_outcome.append("Initiating Transformation Action.")
                      current_stability *= 0.9
                      current_state["environment_stability"] *= 0.95
                      current_state["evaluation_context"]["transforming"] = True
                      # TRN needs a target [PRDX]. This relationship should be represented in the AST structure
                      # e.g., TRN -> [PRDX]

                 elif node.value == "CRTTRLRT":
                     current_outcome.append("Initiating Temporal Reality Creation Action.")
                     current_stability *= 0.9
                     current_state["environment_stability"] *= 0.9
                     current_state["evaluation_context"]["creating_temporal"] = True
                     current_state["evaluation_context"]["expecting_coordinate"] = True # Add flag for parameter handling

             elif isinstance(node, EntityNode):
                  current_outcome.append(f"Referencing Conceptual Entity: {node.value}.")
                  current_state["current_focus_entity"] = node.value

                  if current_state.get("evaluation_context", {}).get("aligning"):
                       current_outcome.append(f"  - Targeted for alignment: {node.value}")
                       current_stability *= (1.0 - node_cost * 0.01) # Entity complexity affects alignment stability
                       # If this is [FABRIC], mark the state
                       if node.value == "[FABRIC]":
                           current_state["fabric_aligned"] = True # Optimistically assume part of alignment
                  elif current_state.get("evaluation_context", {}).get("transforming"):
                       if node.value == "[PRDX]":
                            current_outcome.append("  - Targeted for transformation: Paradox.")
                            # Oracle check happens *after* confirming it's the target
                            oracle_pred = self.oracle.query_halting_oracle("[PRDX]")
                            current_outcome.append(f"  Oracle Prediction for Paradox Transformation: {oracle_pred[0]} (Resource: {oracle_pred[1]})")

                            if oracle_pred[0] == "HALT":
                                current_state["paradox_resolved"] = True
                                predicted_resource = oracle_pred[1] # Store predicted resource
                                current_state["resource"] = predicted_resource
                                current_outcome.append(f"Transformation predicted to HALT. Predicted Resource: {predicted_resource}")
                                current_stability *= 1.3
                                # Resources are added to the pool *after* successful transformation,
                                # potentially asserted by the I [Resource] E [Outcome] sequence.
                                # Let's add predicted resource to state context for later assertion check.
                                current_state["evaluation_context"]["predicted_resource"] = predicted_resource

                            elif oracle_pred[0] == "NON-HALT":
                                current_outcome.append("Transformation predicted NON-HALT. Process aborted at this node.")
                                current_stability *= 0.6
                                current_cost += 0.5
                                return current_state, current_cost, current_stability, current_outcome, True # Stop processing this branch/sequence
                            elif oracle_pred[0] == "CRASH":
                                current_outcome.append("Transformation predicted CRASH. Process aborted, high instability at this node.")
                                current_stability *= 0.3
                                current_cost += 1.5
                                return current_state, current_cost, current_stability, current_outcome, True # Stop processing

                       else:
                           current_outcome.append(f"  - Unexpected entity {node.value} targeted for transformation. Skipping.")
                           current_stability *= 0.8

             elif isinstance(node, OperatorNode):
                  current_outcome.append(f"Using Operator: {node.value}.")
                  # Operator logic needs to consider its children (operands)
                  if node.value == "A":
                      current_outcome.append("  - AND operator linking.")
                      current_stability *= 1.02
                      if current_state.get("evaluation_context", {}).get("aligning"):
                          current_outcome.append("  - Within Alignment context.")

                  elif node.value == "O":
                      current_outcome.append("  - OR operator linking.")
                      current_stability *= 0.7 # OR reduces stability by introducing alternatives/branching
                      if current_state.get("evaluation_context", {}).get("aligning"):
                          current_outcome.append("  - Within Alignment context, causing divergence.")

                  elif node.value == "I":
                       current_outcome.append("  - IMPLIES operator.")
                       # Sets up context for processing Resource/Outcome assertion
                       if current_state.get("evaluation_context", {}).get("transforming"):
                            current_state["evaluation_context"]["expecting_implied"] = True

                  elif node.value == "E":
                       current_outcome.append("  - EQUALS operator.")
                       # Sets up context for processing Outcome assertion
                       if current_state.get("evaluation_context", {}).get("expecting_implied"):
                            current_state["evaluation_context"]["expecting_outcome_assertion"] = True
                            current_state["evaluation_context"]["expecting_implied"] = False # Implies context ends here

                       elif current_state.get("evaluation_context", {}).get("creating_temporal"):
                            # Could be part of CRTTRLRT AT TMPLCRDNT E [HARMONY] AT TMPLCRDNT
                            current_state["evaluation_context"]["expecting_outcome_assertion"] = True


                  elif node.value == "AT":
                       current_outcome.append("  - AT operator (Positional/Temporal).")
                       # Used with CRTTRLRT and potentially outcome assertions.
                       if current_state.get("evaluation_context", {}).get("creating_temporal"):
                            current_state["evaluation_context"]["expecting_coordinate"] = True
                       elif current_state.get("evaluation_context", {}).get("expecting_outcome_assertion"):
                            current_state["evaluation_context"]["expecting_assertion_coordinate"] = True


             elif isinstance(node, ResourceNode):
                  current_outcome.append(f"Referencing Resource: {node.value}.")
                  current_state["current_focus_entity"] = node.value
                  # If this resource is being asserted as an outcome after TRN (I Resource E)...
                  if current_state.get("evaluation_context", {}).get("expecting_implied"):
                       current_state["evaluation_context"]["asserted_resource"] = node.value
                       current_outcome.append(f"  - Asserting resource {node.value} as implied outcome.")
                       # Check if asserted resource matches predicted resource
                       predicted_resource = current_state.get("evaluation_context", {}).get("predicted_resource")
                       if predicted_resource and node.value == predicted_resource:
                           current_outcome.append("  - Asserted resource matches Oracle prediction.")
                           # Add resource to pool upon successful transformation and assertion
                           if node.value in current_state["resource_pool"]:
                                current_state["resource_pool"][node.value] += 1 # Add 1 unit of the predicted/asserted resource
                                current_outcome.append(f"  - Added 1 unit of {node.value} to resource pool. New pool: {current_state['resource_pool']}")
                           else:
                                current_state["resource_pool"][node.value] = 1
                                current_outcome.append(f"  - Created pool for {node.value} and added 1 unit. New pool: {current_state['resource_pool']}")
                       elif predicted_resource:
                           current_outcome.append(f"  - WARNING: Asserted resource ({node.value}) does not match Oracle predicted resource ({predicted_resource}). Instability.")
                           current_stability *= 0.7
                       current_state["evaluation_context"]["expecting_implied"] = False # Implied resource processed, now expect E

             elif isinstance(node, ParameterNode):
                  current_outcome.append(f"Referencing Parameter: {node.value}.")
                  current_state["current_focus_entity"] = node.value
                  if current_state.get("evaluation_context", {}).get("expecting_coordinate"):
                       current_state["temporal_anchor"] = node.value
                       current_outcome.append(f"  - Setting temporal anchor: {node.value}")
                       current_stability *= (1.0 - node_cost * 0.05)
                       current_state["evaluation_context"]["expecting_coordinate"] = False
                  elif current_state.get("evaluation_context", {}).get("expecting_assertion_coordinate"):
                       # Validate assertion coordinate matches the anchor?
                       if current_state["temporal_anchor"] and node.value != current_state["temporal_anchor"]:
                            current_outcome.append(f"  - WARNING: Assertion coordinate ({node.value}) does not match established temporal anchor ({current_state['temporal_anchor']}). Instability.")
                            current_stability *= 0.7
                       current_state["evaluation_context"]["expecting_assertion_coordinate"] = False


             else:
                  current_outcome.append(f"WARNING: Encountered unknown node type for {node.value}. Potential error.")
                  current_stability *= 0.5
                  current_cost += 5.0

             # --- Traverse Children ---
             # The AST structure is a linear list of children under the root in this parser
             # Need to handle operator children correctly if the AST structure is updated
             # For the current simple AST (Root -> [node1, node2, node3...]), traverse linearly
             # If the AST structure is Root -> Action -> Children, process arguments as children

             # Simple linear traversal of children for the current basic AST structure
             # This doesn't fully leverage the tree for complex non-linearity, but applies effects sequentially
             # A true AST simulator would use recursion and operator nodes to manage control flow
             # For example, OperatorNode 'O' would process *both* its children branches conceptually
             # and potentially combine or choose outcomes/states.

             # Let's assume the simple AST structure (Root -> linear list of children)
             # The traversal should handle the sequence and context flags (like 'aligning', 'transforming')
             # to interpret the meaning of adjacent nodes.
             # The processing logic above *already* implicitly assumes a sequence (e.g., TRN expects PRDX after).

             # For a more structured AST where operators link nodes:
             # If node is an operator, process its children (left and right operands)
             # If node is an Action/Entity, process its children (arguments/linked entities)

             # Given the current `ASTParser` which creates Root -> [linear list of children]
             # The traversal below is more appropriate.
             # The logic *inside* `traverse_and_simulate` needs to manage sequence and operator context.

             # Let's refine the traversal logic based on the intended AST structure:
             # Root (Command)
             #  -> Child 1 (Operand/Target)
             #  -> Child 2 (Operator)
             #     -> Left Child (Operand)
             #     -> Right Child (Operand)
             #  -> Child 3 (Operand/Target) ...

             # This structure is harder to build with the current `ASTParser`.
             # Let's revert to the simple AST: Root -> [linear list of children (nodes in sequence)]
             # And the `traverse_and_simulate` processes nodes sequentially, using context flags.
             # The recursive call should process the *current* node's children if any, but the main simulation loop
             # should call traverse on the top-level sequence if not using a true tree structure.

             # Re-thinking the AST structure and traversal:
             # The `ASTParser` as written builds a tree where the first non-operator is the root,
             # and all subsequent nodes are direct children in sequence. This IS a linear list structure
             # under a single root, not a nested tree representing operator precedence.

             # Let's adjust the `simulate_ast` to traverse this linear list of children from the root.
             # The `traverse_and_simulate` function as defined processes a *single* node and then its children.
             # We need to call `traverse_and_simulate` sequentially on the root and then its children.

             # Let's rewrite the simulation entry point to handle the linear list AST structure.

             return current_state, current_cost, current_stability, current_outcome, should_stop # Return values for recursive call


        # New simulation entry point for the linear-list AST structure
        if ast_node is None:
            return {"status": "Error", "predicted_cost": 0, "predicted_stability": 0, "simulated_outcome_trace": ["Error: No AST node provided."], "final_state": {}}

        # Simulate the root node first
        state, total_cost, stability_score, outcome, stopped = traverse_and_simulate(ast_node, state, total_cost, stability_score, outcome)

        if stopped:
             print("\n--- AST Simulation End (Aborted) ---")
             final_status = f"Aborted ({outcome[-1].replace('Process aborted at this node.', '').strip()})"
             return {
                 "status": final_status,
                 "predicted_cost": max(0.0, round(total_cost, 2)),
                 "predicted_stability": max(0.0, round(stability_score, 2)),
                 "simulated_outcome_trace": outcome,
                 "final_state": state
             }


        # Then simulate the children (which are the sequential nodes in the command string)
        i = 0
        while i < len(ast_node.children):
             child_node = ast_node.children[i]
             # Propagate state, cost, stability, outcome
             state, total_cost, stability_score, outcome, child_stopped = \
                 traverse_and_simulate(child_node, state, total_cost, stability_score, outcome)

             if child_stopped:
                  stopped = True
                  break # Stop processing subsequent nodes

             # Special handling for sequences like TRN PRDX I Resource E Outcome
             # The sequential traversal needs to understand these patterns.
             # The logic inside `traverse_and_simulate` for each node type
             # needs to set context flags (evaluation_context) for subsequent nodes.
             # Example: TRN sets "transforming" context.
             # I sets "expecting_implied".
             # Resource checks "expecting_implied" context and sets "asserted_resource", adds to pool.
             # E checks "expecting_implied" and "expecting_outcome_assertion".
             # Outcome checks "expecting_outcome_assertion" and compares to goal/state.

             # The current implementation of `traverse_and_simulate` does some of this
             # using the `evaluation_context`. This linear traversal of children
             # combined with context flags seems a viable approach for the basic grammar.

             i += 1 # Move to the next child node in the sequence

        # --- Simulation End ---
        print("\n--- Resource-Aware AST Simulation End ---")

        final_status = "Completed"
        if stopped:
             final_status = f"Aborted ({outcome[-1].replace('Process aborted at this node.', '').strip()})"
        # Check if Harmony was the goal assertion processed at the end
        # This check needs to be more robust than just checking the state flag
        # It should check if the *last meaningful node sequence* asserted Harmony
        # For the simple parser, check if the last child node was [HARMONY] and context suggests it was an assertion
        last_child = ast_node.children[-1] if ast_node.children else None
        if last_child and last_child.value == "[HARMONY]" and state.get("evaluation_context", {}).get("expecting_outcome_assertion"):
             state["harmony_anchored"] = True # Set Harmony achieved if it was asserted at the end

        if state.get("harmony_anchored"): # Use the state flag now
             final_status = "Success (Harmony Anchored)"
        elif stability_score < 0.5 and not stopped:
            final_status = "Unstable Completion"
        elif stability_score < 0.2 and not stopped:
            final_status = "Critical Instability"
            outcome.append("SIMULATION CRITICAL FAILURE: System state highly unstable.")
            total_cost += 10.0

        # Add a final check if Harmony was intended but not achieved - this is hard
        # without a clear goal node in the AST or protocol.
        # If '[HARMONY]' node was present anywhere and not anchored as outcome...
        if any(node.value == "[HARMONY]" for node in ast_node.children) and not state.get("harmony_anchored") and final_status not in ["Critical Instability", "Aborted", "Success (Harmony Anchored)"]:
             final_status = "Completed (Harmony Goal Not Fully Met or Asserted)"


        return {
            "status": final_status,
            "predicted_cost": max(0.0, round(total_cost, 2)),
            "predicted_stability": max(0.0, round(stability_score, 2)),
            "simulated_outcome_trace": outcome,
            "final_state": state
        }

# Update symbol details with example resource costs for actions
symbol_details["[ALIGN]"]["resource_cost"] = {"[NRG]": 5}
symbol_details["[TRN]"]["resource_cost"] = {"[INF]": 10}
symbol_details["CRTTRLRT"]["resource_cost"] = {"[NRG]": 3, "[INF]": 2} # Example cost for temporal creation

# Instantiate the Resource-Aware AST Simulation Engine
resource_aware_ast_simulation_engine = ResourceAwareASTSimulationEngine(symbol_details, initial_resources={"[INF]": 50, "[NRG]": 50}) # Start with limited resources


print("\n--- Testing Resource-Aware AST Simulation Engine ---")

# Re-run some examples with the resource-aware engine

# 1. Temporal Reality Creation (Resource cost check)
command_temporal = "CRTTRLRT AT TMPLCRDNT"
print(f"\nAttempting Resource-Aware simulation for: {command_temporal}")
try:
    ast_temporal = ast_parser_updated.parse(command_temporal) # Use updated parser
    sim_result_temporal_res = resource_aware_ast_simulation_engine.simulate_ast(ast_temporal)
    print("\nSimulation Result:")
    print(sim_result_temporal_res)
    meta_reasoning_engine.analyze_simulation_result(command_temporal, sim_result_temporal_res)
    meta_reasoning_engine.suggest_command_refinement(command_temporal, sim_result_temporal_res)
except ValueError as e:
    print(f"Parsing Error: {e}")


# 2. Paradox Transformation (Resource cost check and resource generation)
command_paradox_alt = "[TRN] [PRDX] I [NRG] E [HARMONY]"
print(f"\nAttempting Resource-Aware simulation for: {command_paradox_alt}")
try:
    ast_paradox = ast_parser_updated.parse(command_paradox_alt) # Use updated parser
    sim_result_paradox_res = resource_aware_ast_simulation_engine.simulate_ast(ast_paradox)
    print("\nSimulation Result:")
    print(sim_result_paradox_res)
    meta_reasoning_engine.analyze_simulation_result(command_paradox_alt, sim_result_paradox_res)
    meta_reasoning_engine.suggest_command_refinement(command_paradox_alt, sim_result_paradox_res)
except ValueError as e:
    print(f"Parsing Error: {e}")

# 3. Fabric Harmony Alignment (Resource cost check)
command_harmony_stable = "[ALIGN] [FABRIC] A [REALITY] A [CONSCIOUSNESS] A [CHRONOS]"
print(f"\nAttempting Resource-Aware simulation for: {command_harmony_stable}")
try:
    ast_harmony_stable = ast_parser_updated.parse(command_harmony_stable) # Use updated parser
    sim_result_harmony_stable_res = resource_aware_ast_simulation_engine.simulate_ast(ast_harmony_stable)
    print("\nSimulation Result:")
    print(sim_result_harmony_stable_res)
    meta_reasoning_engine.analyze_simulation_result(command_harmony_stable, sim_result_harmony_stable_res)
    meta_reasoning_engine.suggest_command_refinement(command_harmony_stable, sim_result_harmony_stable_res)
except ValueError as e:
    print(f"Parsing Error: {e}")

# Example demonstrating resource insufficiency leading to abort (Requires more complex command or lower initial resources)
# Let's try a sequence of commands in a hypothetical mini-protocol simulation
# This would involve orchestrating multiple calls to the resource-aware simulator.

print("\n--- Conceptual Mini-Protocol Simulation (Resource Strain) ---")

def conceptual_mini_protocol_resource_strain(sim_engine, parser):
     protocol_cost = 0
     protocol_stability = 1.0
     protocol_outcome = ["Conceptual Mini-Protocol: Resource Strain Test"]
     protocol_state = {"resource_pool": sim_engine.initial_resources.copy()} # Start with engine's initial pool

     # Command 1: Create Temporal Anchor (uses NRG 3, INF 2)
     command1 = "CRTTRLRT AT TMPLCRDNT_Alpha"
     protocol_outcome.append(f"\nStep 1: Simulating '{command1}'")
     try:
          ast1 = parser.parse(command1)
          sim1_result = sim_engine.simulate_ast(ast1)
          protocol_cost += sim1_result["predicted_cost"]
          protocol_stability *= sim1_result["predicted_stability"]
          protocol_outcome.extend([f"  {line}" for line in sim1_result["simulated_outcome_trace"]])
          protocol_state["resource_pool"] = sim1_result["final_state"]["resource_pool"].copy() # Update pool state
          if sim1_result["status"].startswith("Aborted"):
               protocol_outcome.append("Step 1 aborted due to resource or other issue. Protocol halted.")
               return {"status": sim1_result["status"], "final_cost": round(protocol_cost, 2), "final_stability": round(protocol_stability, 2), "outcome_trace": protocol_outcome, "final_state": protocol_state}
     except ValueError as e:
          protocol_outcome.append(f"Step 1 Parsing Error: {e}. Protocol halted.")
          protocol_cost += 3.0
          protocol_stability *= 0.5
          return {"status": "Parsing Error", "final_cost": round(protocol_cost, 2), "final_stability": round(protocol_stability, 2), "outcome_trace": protocol_outcome, "final_state": protocol_state}


     # Command 2: Transform Paradox (uses INF 10)
     command2 = "[TRN] [PRDX] I [NRG] E [RESOLVED]" # Assume NRG is generated
     protocol_outcome.append(f"\nStep 2: Simulating '{command2}'")
     try:
          # Temporarily update engine's resource pool for this sim call
          temp_engine = ResourceAwareASTSimulationEngine(symbol_details, initial_resources=protocol_state["resource_pool"])
          ast2 = parser.parse(command2)
          sim2_result = temp_engine.simulate_ast(ast2)
          protocol_cost += sim2_result["predicted_cost"]
          protocol_stability *= sim2_result["predicted_stability"]
          protocol_outcome.extend([f"  {line}" for line in sim2_result["simulated_outcome_trace"]])
          protocol_state["resource_pool"] = sim2_result["final_state"]["resource_pool"].copy() # Update pool state
          if sim2_result["status"].startswith("Aborted"):
               protocol_outcome.append("Step 2 aborted due to resource or other issue. Protocol halted.")
               return {"status": sim2_result["status"], "final_cost": round(protocol_cost, 2), "final_stability": round(protocol_stability, 2), "outcome_trace": protocol_outcome, "final_state": protocol_state}
     except ValueError as e:
          protocol_outcome.append(f"Step 2 Parsing Error: {e}. Protocol halted.")
          protocol_cost += 3.0
          protocol_stability *= 0.5
          return {"status": "Parsing Error", "final_cost": round(protocol_cost, 2), "final_stability": round(protocol_stability, 2), "outcome_trace": protocol_outcome, "final_state": protocol_state}


     # Command 3: Align Fabric (uses NRG 5)
     command3 = "[ALIGN] [FABRIC] A [REALITY]"
     protocol_outcome.append(f"\nStep 3: Simulating '{command3}'")
     try:
          # Temporarily update engine's resource pool for this sim call
          temp_engine = ResourceAwareASTSimulationEngine(symbol_details, initial_resources=protocol_state["resource_pool"])
          ast3 = parser.parse(command3)
          sim3_result = temp_engine.simulate_ast(ast3)
          protocol_cost += sim3_result["predicted_cost"]
          protocol_stability *= sim3_result["predicted_stability"]
          protocol_outcome.extend([f"  {line}" for line in sim3_result["simulated_outcome_trace"]])
          protocol_state["resource_pool"] = sim3_result["final_state"]["resource_pool"].copy() # Update pool state
          if sim3_result["status"].startswith("Aborted"):
               protocol_outcome.append("Step 3 aborted due to resource or other issue. Protocol halted.")
               return {"status": sim3_result["status"], "final_cost": round(protocol_cost, 2), "final_stability": round(protocol_stability, 2), "outcome_trace": protocol_outcome, "final_state": protocol_state}
     except ValueError as e:
          protocol_outcome.append(f"Step 3 Parsing Error: {e}. Protocol halted.")
          protocol_cost += 3.0
          protocol_stability *= 0.5
          return {"status": "Parsing Error", "final_cost": round(protocol_cost, 2), "final_stability": round(protocol_stability, 2), "outcome_trace": protocol_outcome, "final_state": protocol_state}


     protocol_outcome.append("\nMini-Protocol Completed.")
     final_status = "Completed"
     if protocol_stability < 0.5:
          final_status = "Completed (Unstable)"

     return {
         "status": final_status,
         "final_cost": max(0.0, round(protocol_cost, 2)),
         "final_stability": max(0.0, round(protocol_stability, 2)),
         "outcome_trace": protocol_outcome,
         "final_state": protocol_state
     }

# Run the mini-protocol with the resource-aware engine
print("\n--- Executing Conceptual Mini-Protocol (Resource Strain) ---")
mini_protocol_result_res = conceptual_mini_protocol_resource_strain(resource_aware_ast_simulation_engine, ast_parser_updated)

print("\n--- Mini-Protocol Simulation Result (Resource Strain) ---")
for line in mini_protocol_result_res["outcome_trace"]:
    print(line)

print("\nFinal Mini-Protocol Summary:")
print(f"Status: {mini_protocol_result_res['status']}")
print(f"Final Conceptual Cost: {mini_protocol_result_res['final_cost']}")
print(f"Final Stability Score: {mini_protocol_result_res['final_stability']}")
print(f"Final State: {mini_protocol_result_res['final_state']}")
