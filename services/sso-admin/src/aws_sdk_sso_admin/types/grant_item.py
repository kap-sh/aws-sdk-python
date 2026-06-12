"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GrantItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.grant
    import aws_sdk_sso_admin.types.grant_type


class GrantItem(TypedDict):
    grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType"
    """<p>The type of the selected grant.</p>"""
    grant: "aws_sdk_sso_admin.types.grant.Grant"
    """<p>The configuration structure for the selected grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantItem) -> dict:
    out: dict = {}
    import aws_sdk_sso_admin.types.grant_type

    out["GrantType"] = aws_sdk_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    import aws_sdk_sso_admin.types.grant

    out["Grant"] = aws_sdk_sso_admin.types.grant.serialize_aws_json_1_1(value["grant"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GrantItem:
    out: GrantItem = {}  # type: ignore[typeddict-item]
    if "GrantType" in data:
        import aws_sdk_sso_admin.types.grant_type

        out["grant_type"] = aws_sdk_sso_admin.types.grant_type.deserialize_aws_json_1_1(
            data["GrantType"]
        )
    else:
        raise DeserializationError("GrantItem.grant_type required")
    if "Grant" in data:
        import aws_sdk_sso_admin.types.grant

        out["grant"] = aws_sdk_sso_admin.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    else:
        raise DeserializationError("GrantItem.grant required")
    return out
