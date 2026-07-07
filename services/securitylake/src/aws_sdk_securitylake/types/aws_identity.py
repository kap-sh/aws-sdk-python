"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_principal
    import aws_sdk_securitylake.types.external_id


class AwsIdentity(TypedDict, closed=True):
    principal: "aws_sdk_securitylake.types.aws_principal.AwsPrincipal"
    """<p>The Amazon Web Services identity principal.</p>"""
    external_id: "aws_sdk_securitylake.types.external_id.ExternalId"
    """<p>The external ID used to establish trust relationship with the Amazon Web Services identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIdentity) -> dict:
    out: dict = {}
    out["principal"] = value["principal"]
    out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> AwsIdentity:
    out: AwsIdentity = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        out["principal"] = data["principal"]
    else:
        raise DeserializationError("AwsIdentity.principal required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    else:
        raise DeserializationError("AwsIdentity.external_id required")
    return out
