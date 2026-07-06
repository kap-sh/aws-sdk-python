"""Generated from Smithy shape ``com.amazonaws.taxsettings#EstoniaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.registry_commercial_code


class EstoniaAdditionalInfo(TypedDict, closed=True):
    registry_commercial_code: (
        "aws_sdk_taxsettings.types.registry_commercial_code.RegistryCommercialCode"
    )
    """<p> Registry commercial code (RCC) for your TRN in Estonia. This value is an eight-numeric string, such as <code>12345678</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EstoniaAdditionalInfo) -> dict:
    out: dict = {}
    out["registryCommercialCode"] = value["registry_commercial_code"]
    return out


def deserialize_json(data: dict) -> EstoniaAdditionalInfo:
    out: EstoniaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "registryCommercialCode" in data:
        out["registry_commercial_code"] = data["registryCommercialCode"]
    else:
        raise DeserializationError(
            "EstoniaAdditionalInfo.registry_commercial_code required"
        )
    return out
