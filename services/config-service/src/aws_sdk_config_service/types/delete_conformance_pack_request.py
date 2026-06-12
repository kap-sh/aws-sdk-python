"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteConformancePackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_name


class DeleteConformancePackRequest(TypedDict):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConformancePackRequest) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConformancePackRequest:
    out: DeleteConformancePackRequest = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "DeleteConformancePackRequest.conformance_pack_name required"
        )
    return out
