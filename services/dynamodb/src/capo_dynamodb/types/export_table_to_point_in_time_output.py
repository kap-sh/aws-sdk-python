"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportTableToPointInTimeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.export_description


class ExportTableToPointInTimeOutput(TypedDict, closed=True):
    export_description: NotRequired[
        "capo_dynamodb.types.export_description.ExportDescription"
    ]
    """<p>Contains a description of the table export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportTableToPointInTimeOutput) -> dict:
    out: dict = {}
    if "export_description" in value:
        import capo_dynamodb.types.export_description

        out["ExportDescription"] = (
            capo_dynamodb.types.export_description.serialize_aws_json_1_0(
                value["export_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportTableToPointInTimeOutput:
    out: ExportTableToPointInTimeOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExportDescription") is not None:
        import capo_dynamodb.types.export_description

        out["export_description"] = (
            capo_dynamodb.types.export_description.deserialize_aws_json_1_0(
                data["ExportDescription"]
            )
        )
    return out
