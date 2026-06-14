"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.principal_entity_type


class IdentitySourceFilter(TypedDict):
    principal_entity_type: NotRequired[
        "aws_sdk_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    ]
    """<p>The Cedar entity type of the principals returned by the identity provider (IdP) associated with this identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceFilter) -> dict:
    out: dict = {}
    if "principal_entity_type" in value:
        out["principalEntityType"] = value["principal_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IdentitySourceFilter:
    out: IdentitySourceFilter = {}  # type: ignore[typeddict-item]
    if "principalEntityType" in data:
        out["principal_entity_type"] = data["principalEntityType"]
    return out
