"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeEntitlementsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.entitlement_list
    import aws_sdk_appstream.types.string


class DescribeEntitlementsResult(TypedDict):
    entitlements: NotRequired[
        "aws_sdk_appstream.types.entitlement_list.EntitlementList"
    ]
    """<p>The entitlements.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitlementsResult) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import aws_sdk_appstream.types.entitlement_list

        out["Entitlements"] = (
            aws_sdk_appstream.types.entitlement_list.serialize_aws_json_1_1(
                value["entitlements"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitlementsResult:
    out: DescribeEntitlementsResult = {}  # type: ignore[typeddict-item]
    if "Entitlements" in data:
        import aws_sdk_appstream.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_appstream.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
