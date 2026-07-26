"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListUniqueProblemsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.unique_problems_by_execution_result_map


class ListUniqueProblemsResult(TypedDict, closed=True):
    unique_problems: NotRequired[
        "capo_device_farm.types.unique_problems_by_execution_result_map.UniqueProblemsByExecutionResultMap"
    ]
    """<p>Information about the unique problems.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PASSED</p> </li> <li> <p>WARNED</p> </li> <li> <p>FAILED</p> </li> <li> <p>SKIPPED</p> </li> <li> <p>ERRORED</p> </li> <li> <p>STOPPED</p> </li> </ul>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUniqueProblemsResult) -> dict:
    out: dict = {}
    if "unique_problems" in value:
        import capo_device_farm.types.unique_problems_by_execution_result_map

        out["uniqueProblems"] = (
            capo_device_farm.types.unique_problems_by_execution_result_map.serialize_aws_json_1_1(
                value["unique_problems"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUniqueProblemsResult:
    out: ListUniqueProblemsResult = {}  # type: ignore[typeddict-item]
    if "uniqueProblems" in data:
        import capo_device_farm.types.unique_problems_by_execution_result_map

        out["unique_problems"] = (
            capo_device_farm.types.unique_problems_by_execution_result_map.deserialize_aws_json_1_1(
                data["uniqueProblems"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
