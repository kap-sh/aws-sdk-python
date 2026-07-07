"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.objective_resource_filter_list


class CommonControlFilter(TypedDict, closed=True):
    objectives: NotRequired[
        "aws_sdk_controlcatalog.types.objective_resource_filter_list.ObjectiveResourceFilterList"
    ]
    """<p>The objective that's used as filter criteria.</p> <p>You can use this parameter to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlFilter) -> dict:
    out: dict = {}
    if "objectives" in value:
        import aws_sdk_controlcatalog.types.objective_resource_filter_list

        out["Objectives"] = (
            aws_sdk_controlcatalog.types.objective_resource_filter_list.serialize_json(
                value["objectives"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommonControlFilter:
    out: CommonControlFilter = {}  # type: ignore[typeddict-item]
    if "Objectives" in data:
        import aws_sdk_controlcatalog.types.objective_resource_filter_list

        out["objectives"] = (
            aws_sdk_controlcatalog.types.objective_resource_filter_list.deserialize_json(
                data["Objectives"]
            )
        )
    return out
