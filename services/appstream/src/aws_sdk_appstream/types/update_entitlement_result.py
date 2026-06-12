"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateEntitlementResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.entitlement


class UpdateEntitlementResult(TypedDict):
    entitlement: NotRequired["aws_sdk_appstream.types.entitlement.Entitlement"]
    """<p>The entitlement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEntitlementResult) -> dict:
    out: dict = {}
    if "entitlement" in value:
        import aws_sdk_appstream.types.entitlement

        out["Entitlement"] = aws_sdk_appstream.types.entitlement.serialize_aws_json_1_1(
            value["entitlement"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEntitlementResult:
    out: UpdateEntitlementResult = {}  # type: ignore[typeddict-item]
    if "Entitlement" in data:
        import aws_sdk_appstream.types.entitlement

        out["entitlement"] = (
            aws_sdk_appstream.types.entitlement.deserialize_aws_json_1_1(
                data["Entitlement"]
            )
        )
    return out
