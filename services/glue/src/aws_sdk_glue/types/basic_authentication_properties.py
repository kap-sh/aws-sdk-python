"""Generated from Smithy shape ``com.amazonaws.glue#BasicAuthenticationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_property


class BasicAuthenticationProperties(TypedDict, closed=True):
    username: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The username property name to use for Basic authentication credentials.</p>"""
    password: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The password property name to use for Basic authentication credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BasicAuthenticationProperties) -> dict:
    out: dict = {}
    if "username" in value:
        import aws_sdk_glue.types.connector_property

        out["Username"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["username"]
        )
    if "password" in value:
        import aws_sdk_glue.types.connector_property

        out["Password"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["password"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BasicAuthenticationProperties:
    out: BasicAuthenticationProperties = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        import aws_sdk_glue.types.connector_property

        out["username"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["Username"]
            )
        )
    if "Password" in data:
        import aws_sdk_glue.types.connector_property

        out["password"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["Password"]
            )
        )
    return out
