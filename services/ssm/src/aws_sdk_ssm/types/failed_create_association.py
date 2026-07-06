"""Generated from Smithy shape ``com.amazonaws.ssm#FailedCreateAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.batch_error_message
    import aws_sdk_ssm.types.create_association_batch_request_entry
    import aws_sdk_ssm.types.fault


class FailedCreateAssociation(TypedDict, closed=True):
    entry: NotRequired[
        "aws_sdk_ssm.types.create_association_batch_request_entry.CreateAssociationBatchRequestEntry"
    ]
    """<p>The association.</p>"""
    message: NotRequired["aws_sdk_ssm.types.batch_error_message.BatchErrorMessage"]
    """<p>A description of the failure.</p>"""
    fault: NotRequired["aws_sdk_ssm.types.fault.Fault"]
    """<p>The source of the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateAssociation) -> dict:
    out: dict = {}
    if "entry" in value:
        import aws_sdk_ssm.types.create_association_batch_request_entry

        out["Entry"] = (
            aws_sdk_ssm.types.create_association_batch_request_entry.serialize_aws_json_1_1(
                value["entry"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "fault" in value:
        import aws_sdk_ssm.types.fault

        out["Fault"] = aws_sdk_ssm.types.fault.serialize_aws_json_1_1(value["fault"])
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedCreateAssociation:
    out: FailedCreateAssociation = {}  # type: ignore[typeddict-item]
    if "Entry" in data:
        import aws_sdk_ssm.types.create_association_batch_request_entry

        out["entry"] = (
            aws_sdk_ssm.types.create_association_batch_request_entry.deserialize_aws_json_1_1(
                data["Entry"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Fault" in data:
        import aws_sdk_ssm.types.fault

        out["fault"] = aws_sdk_ssm.types.fault.deserialize_aws_json_1_1(data["Fault"])
    return out
