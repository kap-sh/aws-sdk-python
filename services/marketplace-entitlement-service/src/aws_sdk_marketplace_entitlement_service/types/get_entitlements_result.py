"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#GetEntitlementsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_entitlement_service.types.entitlement_list
    import aws_sdk_marketplace_entitlement_service.types.non_empty_string


class GetEntitlementsResult(TypedDict):
    entitlements: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.entitlement_list.EntitlementList"
    ]
    """<p>The set of entitlements found through the GetEntitlements operation. If the result contains an empty set of entitlements, NextToken might still be present and should be used.</p>"""
    next_token: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
    ]
    """<p>For paginated results, use NextToken in subsequent calls to GetEntitlements. If the result contains an empty set of entitlements, NextToken might still be present and should be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntitlementsResult) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import aws_sdk_marketplace_entitlement_service.types.entitlement_list

        out["Entitlements"] = (
            aws_sdk_marketplace_entitlement_service.types.entitlement_list.serialize_aws_json_1_1(
                value["entitlements"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntitlementsResult:
    out: GetEntitlementsResult = {}  # type: ignore[typeddict-item]
    if "Entitlements" in data:
        import aws_sdk_marketplace_entitlement_service.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_marketplace_entitlement_service.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
