"""Generated from Smithy shape ``com.amazonaws.cloud9#ListEnvironmentsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_id_list
    import aws_sdk_cloud9.types.string


class ListEnvironmentsResult(TypedDict):
    next_token: NotRequired["aws_sdk_cloud9.types.string.String"]
    """<p>If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a <i>next token</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""
    environment_ids: NotRequired[
        "aws_sdk_cloud9.types.environment_id_list.EnvironmentIdList"
    ]
    """<p>The list of environment identifiers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEnvironmentsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "environment_ids" in value:
        import aws_sdk_cloud9.types.environment_id_list

        out["environmentIds"] = (
            aws_sdk_cloud9.types.environment_id_list.serialize_aws_json_1_1(
                value["environment_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEnvironmentsResult:
    out: ListEnvironmentsResult = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "environmentIds" in data:
        import aws_sdk_cloud9.types.environment_id_list

        out["environment_ids"] = (
            aws_sdk_cloud9.types.environment_id_list.deserialize_aws_json_1_1(
                data["environmentIds"]
            )
        )
    return out
