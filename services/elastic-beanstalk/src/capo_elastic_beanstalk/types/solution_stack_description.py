"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SolutionStackDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.solution_stack_file_type_list
    import capo_elastic_beanstalk.types.solution_stack_name


class SolutionStackDescription(TypedDict, closed=True):
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of the solution stack.</p>"""
    permitted_file_types: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_file_type_list.SolutionStackFileTypeList"
    ]
    """<p>The permitted file types allowed for a solution stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SolutionStackDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "solution_stack_name" in value:
        pairs.append(
            (f"{key_prefix}SolutionStackName", str(value["solution_stack_name"]))
        )
    if "permitted_file_types" in value:
        import capo_elastic_beanstalk.types.solution_stack_file_type_list

        capo_elastic_beanstalk.types.solution_stack_file_type_list.serialize_query(
            value["permitted_file_types"], pairs, f"{key_prefix}PermittedFileTypes"
        )


def deserialize_query(el: Element) -> SolutionStackDescription:
    out: SolutionStackDescription = {}  # type: ignore[typeddict-item]
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_permitted_file_types = el.find("PermittedFileTypes")
    if child_permitted_file_types is not None:
        import capo_elastic_beanstalk.types.solution_stack_file_type_list

        out["permitted_file_types"] = (
            capo_elastic_beanstalk.types.solution_stack_file_type_list.deserialize_query(
                child_permitted_file_types
            )
        )
    return out
