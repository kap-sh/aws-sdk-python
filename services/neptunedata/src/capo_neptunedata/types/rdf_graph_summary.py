"""Generated from Smithy shape ``com.amazonaws.neptunedata#RDFGraphSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.classes
    import capo_neptunedata.types.long_valued_map_list
    import capo_neptunedata.types.subject_structures


class RDFGraphSummary(TypedDict, closed=True):
    num_distinct_subjects: NotRequired["int"]
    """<p>The number of distinct subjects in the graph.</p>"""
    num_distinct_predicates: NotRequired["int"]
    """<p>The number of distinct predicates in the graph.</p>"""
    num_quads: NotRequired["int"]
    """<p>The number of quads in the graph.</p>"""
    num_classes: NotRequired["int"]
    """<p>The number of classes in the graph.</p>"""
    classes: NotRequired["capo_neptunedata.types.classes.Classes"]
    """<p>A list of the classes in the graph.</p>"""
    predicates: NotRequired[
        "capo_neptunedata.types.long_valued_map_list.LongValuedMapList"
    ]
    r"""<p>\"A list of predicates in the graph, along with the predicate counts.</p>"""
    subject_structures: NotRequired[
        "capo_neptunedata.types.subject_structures.SubjectStructures"
    ]
    """<p>This field is only present when the request mode is <code>DETAILED</code>. It contains a list of subject structures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RDFGraphSummary) -> dict:
    out: dict = {}
    if "num_distinct_subjects" in value:
        out["numDistinctSubjects"] = value["num_distinct_subjects"]
    if "num_distinct_predicates" in value:
        out["numDistinctPredicates"] = value["num_distinct_predicates"]
    if "num_quads" in value:
        out["numQuads"] = value["num_quads"]
    if "num_classes" in value:
        out["numClasses"] = value["num_classes"]
    if "classes" in value:
        import capo_neptunedata.types.classes

        out["classes"] = capo_neptunedata.types.classes.serialize_json(value["classes"])
    if "predicates" in value:
        import capo_neptunedata.types.long_valued_map_list

        out["predicates"] = capo_neptunedata.types.long_valued_map_list.serialize_json(
            value["predicates"]
        )
    if "subject_structures" in value:
        import capo_neptunedata.types.subject_structures

        out["subjectStructures"] = (
            capo_neptunedata.types.subject_structures.serialize_json(
                value["subject_structures"]
            )
        )
    return out


def deserialize_json(data: dict) -> RDFGraphSummary:
    out: RDFGraphSummary = {}  # type: ignore[typeddict-item]
    if "numDistinctSubjects" in data:
        out["num_distinct_subjects"] = data["numDistinctSubjects"]
    if "numDistinctPredicates" in data:
        out["num_distinct_predicates"] = data["numDistinctPredicates"]
    if "numQuads" in data:
        out["num_quads"] = data["numQuads"]
    if "numClasses" in data:
        out["num_classes"] = data["numClasses"]
    if "classes" in data:
        import capo_neptunedata.types.classes

        out["classes"] = capo_neptunedata.types.classes.deserialize_json(
            data["classes"]
        )
    if "predicates" in data:
        import capo_neptunedata.types.long_valued_map_list

        out["predicates"] = (
            capo_neptunedata.types.long_valued_map_list.deserialize_json(
                data["predicates"]
            )
        )
    if "subjectStructures" in data:
        import capo_neptunedata.types.subject_structures

        out["subject_structures"] = (
            capo_neptunedata.types.subject_structures.deserialize_json(
                data["subjectStructures"]
            )
        )
    return out
