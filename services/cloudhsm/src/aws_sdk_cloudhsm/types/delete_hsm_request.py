"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DeleteHsmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hsm_arn


class DeleteHsmRequest(TypedDict):
    hsm_arn: "aws_sdk_cloudhsm.types.hsm_arn.HsmArn"
    """<p>The ARN of the HSM to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHsmRequest) -> dict:
    out: dict = {}
    out["HsmArn"] = value["hsm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHsmRequest:
    out: DeleteHsmRequest = {}  # type: ignore[typeddict-item]
    if "HsmArn" in data:
        out["hsm_arn"] = data["HsmArn"]
    else:
        raise DeserializationError("DeleteHsmRequest.hsm_arn required")
    return out
