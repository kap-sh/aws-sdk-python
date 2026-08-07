"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ListAvailableSolutionStacksResultMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.available_solution_stack_details_list
    import capo_elastic_beanstalk.types.available_solution_stack_names_list


class ListAvailableSolutionStacksResultMessage(TypedDict, closed=True):
    solution_stacks: NotRequired[
        "capo_elastic_beanstalk.types.available_solution_stack_names_list.AvailableSolutionStackNamesList"
    ]
    """<p>A list of available solution stacks.</p>"""
    solution_stack_details: NotRequired[
        "capo_elastic_beanstalk.types.available_solution_stack_details_list.AvailableSolutionStackDetailsList"
    ]
    """<p> A list of available solution stacks and their <a>SolutionStackDescription</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAvailableSolutionStacksResultMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "solution_stacks" in value:
        import capo_elastic_beanstalk.types.available_solution_stack_names_list

        capo_elastic_beanstalk.types.available_solution_stack_names_list.serialize_query(
            value["solution_stacks"], pairs, f"{key_prefix}SolutionStacks"
        )
    if "solution_stack_details" in value:
        import capo_elastic_beanstalk.types.available_solution_stack_details_list

        capo_elastic_beanstalk.types.available_solution_stack_details_list.serialize_query(
            value["solution_stack_details"], pairs, f"{key_prefix}SolutionStackDetails"
        )


def deserialize_query(el: Element) -> ListAvailableSolutionStacksResultMessage:
    out: ListAvailableSolutionStacksResultMessage = {}  # type: ignore[typeddict-item]
    child_solution_stacks = el.find("SolutionStacks")
    if child_solution_stacks is not None:
        import capo_elastic_beanstalk.types.available_solution_stack_names_list

        out["solution_stacks"] = (
            capo_elastic_beanstalk.types.available_solution_stack_names_list.deserialize_query(
                child_solution_stacks
            )
        )
    child_solution_stack_details = el.find("SolutionStackDetails")
    if child_solution_stack_details is not None:
        import capo_elastic_beanstalk.types.available_solution_stack_details_list

        out["solution_stack_details"] = (
            capo_elastic_beanstalk.types.available_solution_stack_details_list.deserialize_query(
                child_solution_stack_details
            )
        )
    return out
