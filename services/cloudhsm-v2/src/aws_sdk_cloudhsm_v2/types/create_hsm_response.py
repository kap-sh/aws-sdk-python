"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CreateHsmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.hsm


class CreateHsmResponse(TypedDict, closed=True):
    hsm: NotRequired["aws_sdk_cloudhsm_v2.types.hsm.Hsm"]
    """<p>Information about the HSM that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHsmResponse) -> dict:
    out: dict = {}
    if "hsm" in value:
        import aws_sdk_cloudhsm_v2.types.hsm

        out["Hsm"] = aws_sdk_cloudhsm_v2.types.hsm.serialize_aws_json_1_1(value["hsm"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHsmResponse:
    out: CreateHsmResponse = {}  # type: ignore[typeddict-item]
    if "Hsm" in data:
        import aws_sdk_cloudhsm_v2.types.hsm

        out["hsm"] = aws_sdk_cloudhsm_v2.types.hsm.deserialize_aws_json_1_1(data["Hsm"])
    return out
