"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.links_type
    import aws_sdk_cognito_identity_provider.types.terms_enforcement_type
    import aws_sdk_cognito_identity_provider.types.terms_id_type
    import aws_sdk_cognito_identity_provider.types.terms_name_type
    import aws_sdk_cognito_identity_provider.types.terms_source_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class UpdateTermsRequest(TypedDict, closed=True):
    terms_id: "aws_sdk_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the terms document that you want to update.</p>"""
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms that you want to update.</p>"""
    terms_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.terms_name_type.TermsNameType"
    ]
    """<p>The new name that you want to apply to the requested terms documents.</p>"""
    terms_source: NotRequired[
        "aws_sdk_cognito_identity_provider.types.terms_source_type.TermsSourceType"
    ]
    """<p>This parameter is reserved for future use and currently accepts only one value.</p>"""
    enforcement: NotRequired[
        "aws_sdk_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType"
    ]
    """<p>This parameter is reserved for future use and currently accepts only one value.</p>"""
    links: NotRequired["aws_sdk_cognito_identity_provider.types.links_type.LinksType"]
    r"""<p>A map of URLs to languages. For each localized language that will view the requested <code>TermsName</code>, assign a URL. A selection of <code>cognito:default</code> displays for all languages that don't have a language-specific URL.</p> <p>For example, <code>\"cognito:default\": \"https://terms.example.com\", \"cognito:spanish\": \"https://terms.example.com/es\"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTermsRequest) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
    out["UserPoolId"] = value["user_pool_id"]
    if "terms_name" in value:
        out["TermsName"] = value["terms_name"]
    if "terms_source" in value:
        import aws_sdk_cognito_identity_provider.types.terms_source_type

        out["TermsSource"] = (
            aws_sdk_cognito_identity_provider.types.terms_source_type.serialize_aws_json_1_1(
                value["terms_source"]
            )
        )
    if "enforcement" in value:
        import aws_sdk_cognito_identity_provider.types.terms_enforcement_type

        out["Enforcement"] = (
            aws_sdk_cognito_identity_provider.types.terms_enforcement_type.serialize_aws_json_1_1(
                value["enforcement"]
            )
        )
    if "links" in value:
        import aws_sdk_cognito_identity_provider.types.links_type

        out["Links"] = (
            aws_sdk_cognito_identity_provider.types.links_type.serialize_aws_json_1_1(
                value["links"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTermsRequest:
    out: UpdateTermsRequest = {}  # type: ignore[typeddict-item]
    if "TermsId" in data:
        out["terms_id"] = data["TermsId"]
    else:
        raise DeserializationError("UpdateTermsRequest.terms_id required")
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateTermsRequest.user_pool_id required")
    if "TermsName" in data:
        out["terms_name"] = data["TermsName"]
    if "TermsSource" in data:
        import aws_sdk_cognito_identity_provider.types.terms_source_type

        out["terms_source"] = (
            aws_sdk_cognito_identity_provider.types.terms_source_type.deserialize_aws_json_1_1(
                data["TermsSource"]
            )
        )
    if "Enforcement" in data:
        import aws_sdk_cognito_identity_provider.types.terms_enforcement_type

        out["enforcement"] = (
            aws_sdk_cognito_identity_provider.types.terms_enforcement_type.deserialize_aws_json_1_1(
                data["Enforcement"]
            )
        )
    if "Links" in data:
        import aws_sdk_cognito_identity_provider.types.links_type

        out["links"] = (
            aws_sdk_cognito_identity_provider.types.links_type.deserialize_aws_json_1_1(
                data["Links"]
            )
        )
    return out
