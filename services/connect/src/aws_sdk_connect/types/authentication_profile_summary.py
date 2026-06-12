"""Generated from Smithy shape ``com.amazonaws.connect#AuthenticationProfileSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.authentication_profile_id
    import aws_sdk_connect.types.authentication_profile_name
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class AuthenticationProfileSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_connect.types.authentication_profile_id.AuthenticationProfileId"
    ]
    """<p>The unique identifier of the authentication profile.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the authentication profile summary.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.authentication_profile_name.AuthenticationProfileName"
    ]
    """<p>The name of the authentication profile summary.</p>"""
    is_default: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Shows whether the authentication profile is the default authentication profile for the Connect Customer instance. The default authentication profile applies to all agents in an Connect Customer instance, unless overridden by another authentication profile.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the authentication profile summary was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region when the authentication profile summary was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationProfileSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    out["IsDefault"] = value.get("is_default", False)
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> AuthenticationProfileSummary:
    out: AuthenticationProfileSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
