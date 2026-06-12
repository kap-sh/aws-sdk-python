"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.service_code
    import aws_sdk_service_quotas.types.service_name


class ServiceInfo(TypedDict):
    service_code: NotRequired["aws_sdk_service_quotas.types.service_code.ServiceCode"]
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    service_name: NotRequired["aws_sdk_service_quotas.types.service_name.ServiceName"]
    """<p>Specifies the service name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceInfo) -> dict:
    out: dict = {}
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceInfo:
    out: ServiceInfo = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    return out
