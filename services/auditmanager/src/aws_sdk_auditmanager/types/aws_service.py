"""Generated from Smithy shape ``com.amazonaws.auditmanager#AWSService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.aws_service_name


class AWSService(TypedDict, closed=True):
    service_name: NotRequired[
        "aws_sdk_auditmanager.types.aws_service_name.AWSServiceName"
    ]
    """<p> The name of the Amazon Web Services service. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSService) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    return out


def deserialize_json(data: dict) -> AWSService:
    out: AWSService = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    return out
