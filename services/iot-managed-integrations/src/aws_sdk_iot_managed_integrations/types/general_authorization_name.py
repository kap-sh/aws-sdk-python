"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GeneralAuthorizationName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_material_name


class GeneralAuthorizationName(TypedDict, closed=True):
    auth_material_name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.auth_material_name.AuthMaterialName"
    ]
    """<p>The name of the authorization material.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneralAuthorizationName) -> dict:
    out: dict = {}
    if "auth_material_name" in value:
        out["AuthMaterialName"] = value["auth_material_name"]
    return out


def deserialize_json(data: dict) -> GeneralAuthorizationName:
    out: GeneralAuthorizationName = {}  # type: ignore[typeddict-item]
    if "AuthMaterialName" in data:
        out["auth_material_name"] = data["AuthMaterialName"]
    return out
