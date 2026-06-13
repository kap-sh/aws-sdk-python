"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetFindingDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.finding_arn_list


class BatchGetFindingDetailsRequest(TypedDict):
    finding_arns: "aws_sdk_inspector2.types.finding_arn_list.FindingArnList"
    """<p>A list of finding ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingDetailsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.finding_arn_list

    out["findingArns"] = aws_sdk_inspector2.types.finding_arn_list.serialize_json(
        value["finding_arns"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetFindingDetailsRequest:
    out: BatchGetFindingDetailsRequest = {}  # type: ignore[typeddict-item]
    if "findingArns" in data:
        import aws_sdk_inspector2.types.finding_arn_list

        out["finding_arns"] = (
            aws_sdk_inspector2.types.finding_arn_list.deserialize_json(
                data["findingArns"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetFindingDetailsRequest.finding_arns required"
        )
    return out
