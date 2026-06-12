"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#RequestFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_recommended_actions.types.action_filter_list


class RequestFilter(TypedDict):
    actions: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.action_filter_list.ActionFilterList"
    ]
    """<p>A list of action filters that define criteria for filtering results. Each filter specifies a key, match option, and corresponding values to filter on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestFilter) -> dict:
    out: dict = {}
    if "actions" in value:
        import aws_sdk_bcm_recommended_actions.types.action_filter_list

        out["actions"] = (
            aws_sdk_bcm_recommended_actions.types.action_filter_list.serialize_aws_json_1_0(
                value["actions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestFilter:
    out: RequestFilter = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import aws_sdk_bcm_recommended_actions.types.action_filter_list

        out["actions"] = (
            aws_sdk_bcm_recommended_actions.types.action_filter_list.deserialize_aws_json_1_0(
                data["actions"]
            )
        )
    return out
