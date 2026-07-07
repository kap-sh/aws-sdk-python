"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAccessKeySessionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_access_key_session_context_attributes
    import aws_sdk_securityhub.types.aws_iam_access_key_session_context_session_issuer


class AwsIamAccessKeySessionContext(TypedDict, closed=True):
    attributes: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_access_key_session_context_attributes.AwsIamAccessKeySessionContextAttributes"
    ]
    """<p>Attributes of the session that the key was used for.</p>"""
    session_issuer: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_access_key_session_context_session_issuer.AwsIamAccessKeySessionContextSessionIssuer"
    ]
    """<p>Information about the entity that created the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAccessKeySessionContext) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_securityhub.types.aws_iam_access_key_session_context_attributes

        out["Attributes"] = (
            aws_sdk_securityhub.types.aws_iam_access_key_session_context_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "session_issuer" in value:
        import aws_sdk_securityhub.types.aws_iam_access_key_session_context_session_issuer

        out["SessionIssuer"] = (
            aws_sdk_securityhub.types.aws_iam_access_key_session_context_session_issuer.serialize_json(
                value["session_issuer"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsIamAccessKeySessionContext:
    out: AwsIamAccessKeySessionContext = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_securityhub.types.aws_iam_access_key_session_context_attributes

        out["attributes"] = (
            aws_sdk_securityhub.types.aws_iam_access_key_session_context_attributes.deserialize_json(
                data["Attributes"]
            )
        )
    if "SessionIssuer" in data:
        import aws_sdk_securityhub.types.aws_iam_access_key_session_context_session_issuer

        out["session_issuer"] = (
            aws_sdk_securityhub.types.aws_iam_access_key_session_context_session_issuer.deserialize_json(
                data["SessionIssuer"]
            )
        )
    return out
