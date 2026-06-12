"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateHapgRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.label


class CreateHapgRequest(TypedDict):
    label: "aws_sdk_cloudhsm.types.label.Label"
    """<p>The label of the new high-availability partition group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHapgRequest) -> dict:
    out: dict = {}
    out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHapgRequest:
    out: CreateHapgRequest = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        out["label"] = data["Label"]
    else:
        raise DeserializationError("CreateHapgRequest.label required")
    return out
