"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.date_type
    import aws_sdk_cognito_identity_provider.types.links_type
    import aws_sdk_cognito_identity_provider.types.terms_enforcement_type
    import aws_sdk_cognito_identity_provider.types.terms_id_type
    import aws_sdk_cognito_identity_provider.types.terms_name_type
    import aws_sdk_cognito_identity_provider.types.terms_source_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class TermsType(TypedDict, closed=True):
    terms_id: "aws_sdk_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the terms documents.</p>"""
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms documents.</p>"""
    client_id: "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that the terms documents are assigned to.</p>"""
    terms_name: "aws_sdk_cognito_identity_provider.types.terms_name_type.TermsNameType"
    """<p>The type and friendly name of the terms documents.</p>"""
    terms_source: (
        "aws_sdk_cognito_identity_provider.types.terms_source_type.TermsSourceType"
    )
    """<p>This parameter is reserved for future use and currently accepts one value.</p>"""
    enforcement: "aws_sdk_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType"
    """<p>This parameter is reserved for future use and currently accepts one value.</p>"""
    links: "aws_sdk_cognito_identity_provider.types.links_type.LinksType"
    r"""<p>A map of URLs to languages. For each localized language that will view the requested <code>TermsName</code>, assign a URL. A selection of <code>cognito:default</code> displays for all languages that don't have a language-specific URL.</p> <p>For example, <code>\"cognito:default\": \"https://terms.example.com\", \"cognito:spanish\": \"https://terms.example.com/es\"</code>.</p>"""
    creation_date: "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    last_modified_date: "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsType) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    out["TermsName"] = value["terms_name"]
    import aws_sdk_cognito_identity_provider.types.terms_source_type

    out["TermsSource"] = (
        aws_sdk_cognito_identity_provider.types.terms_source_type.serialize_aws_json_1_1(
            value["terms_source"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.terms_enforcement_type

    out["Enforcement"] = (
        aws_sdk_cognito_identity_provider.types.terms_enforcement_type.serialize_aws_json_1_1(
            value["enforcement"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.links_type

    out["Links"] = (
        aws_sdk_cognito_identity_provider.types.links_type.serialize_aws_json_1_1(
            value["links"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.date_type

    out["CreationDate"] = (
        aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["creation_date"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.date_type

    out["LastModifiedDate"] = (
        aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["last_modified_date"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TermsType:
    out: TermsType = {}  # type: ignore[typeddict-item]
    if "TermsId" in data:
        out["terms_id"] = data["TermsId"]
    else:
        raise DeserializationError("TermsType.terms_id required")
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("TermsType.user_pool_id required")
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("TermsType.client_id required")
    if "TermsName" in data:
        out["terms_name"] = data["TermsName"]
    else:
        raise DeserializationError("TermsType.terms_name required")
    if "TermsSource" in data:
        import aws_sdk_cognito_identity_provider.types.terms_source_type

        out["terms_source"] = (
            aws_sdk_cognito_identity_provider.types.terms_source_type.deserialize_aws_json_1_1(
                data["TermsSource"]
            )
        )
    else:
        raise DeserializationError("TermsType.terms_source required")
    if "Enforcement" in data:
        import aws_sdk_cognito_identity_provider.types.terms_enforcement_type

        out["enforcement"] = (
            aws_sdk_cognito_identity_provider.types.terms_enforcement_type.deserialize_aws_json_1_1(
                data["Enforcement"]
            )
        )
    else:
        raise DeserializationError("TermsType.enforcement required")
    if "Links" in data:
        import aws_sdk_cognito_identity_provider.types.links_type

        out["links"] = (
            aws_sdk_cognito_identity_provider.types.links_type.deserialize_aws_json_1_1(
                data["Links"]
            )
        )
    else:
        raise DeserializationError("TermsType.links required")
    if "CreationDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    else:
        raise DeserializationError("TermsType.creation_date required")
    if "LastModifiedDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    else:
        raise DeserializationError("TermsType.last_modified_date required")
    return out
