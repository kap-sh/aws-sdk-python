"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#UpdateIndexTypeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resource_explorer_2.types.index_state
    import aws_sdk_resource_explorer_2.types.index_type


class UpdateIndexTypeOutput(TypedDict):
    arn: NotRequired["str"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the index that you updated.</p>"""
    type: NotRequired["aws_sdk_resource_explorer_2.types.index_type.IndexType"]
    """<p>Specifies the type of the specified index after the operation completes.</p>"""
    state: NotRequired["aws_sdk_resource_explorer_2.types.index_state.IndexState"]
    """<p>Indicates the state of the request to update the index. This operation is asynchronous. Call the <a>GetIndex</a> operation to check for changes.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and timestamp when the index was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexTypeOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_updated_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIndexTypeOutput:
    out: UpdateIndexTypeOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "State" in data:
        out["state"] = data["State"]
    if "LastUpdatedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    return out
