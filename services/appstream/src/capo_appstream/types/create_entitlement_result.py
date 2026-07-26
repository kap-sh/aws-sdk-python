"""Generated from Smithy shape ``com.amazonaws.appstream#CreateEntitlementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.entitlement


class CreateEntitlementResult(TypedDict, closed=True):
    entitlement: NotRequired["capo_appstream.types.entitlement.Entitlement"]
    """<p>The entitlement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEntitlementResult) -> dict:
    out: dict = {}
    if "entitlement" in value:
        import capo_appstream.types.entitlement

        out["Entitlement"] = capo_appstream.types.entitlement.serialize_aws_json_1_1(
            value["entitlement"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEntitlementResult:
    out: CreateEntitlementResult = {}  # type: ignore[typeddict-item]
    if "Entitlement" in data:
        import capo_appstream.types.entitlement

        out["entitlement"] = capo_appstream.types.entitlement.deserialize_aws_json_1_1(
            data["Entitlement"]
        )
    return out
