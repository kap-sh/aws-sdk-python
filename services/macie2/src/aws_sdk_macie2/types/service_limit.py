"""Generated from Smithy shape ``com.amazonaws.macie2#ServiceLimit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.unit


class ServiceLimit(TypedDict):
    is_service_limited: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the account has met the quota that corresponds to the metric specified by the UsageByAccount.type field in the response.</p>"""
    unit: NotRequired["aws_sdk_macie2.types.unit.Unit"]
    """<p>The unit of measurement for the value specified by the value field.</p>"""
    value: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The value for the metric specified by the UsageByAccount.type field in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLimit) -> dict:
    out: dict = {}
    if "is_service_limited" in value:
        out["isServiceLimited"] = value["is_service_limited"]
    if "unit" in value:
        import aws_sdk_macie2.types.unit

        out["unit"] = aws_sdk_macie2.types.unit.serialize_json(value["unit"])
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ServiceLimit:
    out: ServiceLimit = {}  # type: ignore[typeddict-item]
    if "isServiceLimited" in data:
        out["is_service_limited"] = data["isServiceLimited"]
    if "unit" in data:
        import aws_sdk_macie2.types.unit

        out["unit"] = aws_sdk_macie2.types.unit.deserialize_json(data["unit"])
    if "value" in data:
        out["value"] = data["value"]
    return out
