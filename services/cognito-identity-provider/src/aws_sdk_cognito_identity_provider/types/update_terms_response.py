"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateTermsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.terms_type


class UpdateTermsResponse(TypedDict):
    terms: NotRequired["aws_sdk_cognito_identity_provider.types.terms_type.TermsType"]
    """<p>A summary of the updates to your terms documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTermsResponse) -> dict:
    out: dict = {}
    if "terms" in value:
        import aws_sdk_cognito_identity_provider.types.terms_type

        out["Terms"] = (
            aws_sdk_cognito_identity_provider.types.terms_type.serialize_aws_json_1_1(
                value["terms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTermsResponse:
    out: UpdateTermsResponse = {}  # type: ignore[typeddict-item]
    if "Terms" in data:
        import aws_sdk_cognito_identity_provider.types.terms_type

        out["terms"] = (
            aws_sdk_cognito_identity_provider.types.terms_type.deserialize_aws_json_1_1(
                data["Terms"]
            )
        )
    return out
