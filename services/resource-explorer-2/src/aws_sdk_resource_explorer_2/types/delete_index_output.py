"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#DeleteIndexOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resource_explorer_2.types.index_state


class DeleteIndexOutput(TypedDict):
    arn: NotRequired["str"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the index that you successfully started the deletion process.</p> <note> <p>This operation is asynchronous. To check its status, call the <a>GetIndex</a> operation.</p> </note>"""
    state: NotRequired["aws_sdk_resource_explorer_2.types.index_state.IndexState"]
    """<p>Indicates the current state of the index. </p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when you last updated this index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIndexOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
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


def deserialize_json(data: dict) -> DeleteIndexOutput:
    out: DeleteIndexOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
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
