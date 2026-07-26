"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ACMManaged``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string_min3_max256
    import capo_apigatewayv2.types.__string_min10_max2048


class ACMManaged(TypedDict, closed=True):
    certificate_arn: NotRequired[
        "capo_apigatewayv2.types.__string_min10_max2048.__stringMin10Max2048"
    ]
    """<p>The certificate ARN.</p>"""
    domain_name: NotRequired[
        "capo_apigatewayv2.types.__string_min3_max256.__stringMin3Max256"
    ]
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ACMManaged) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> ACMManaged:
    out: ACMManaged = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    return out
