"""Generated from Smithy shape ``com.amazonaws.athena#QueryResultsS3AccessGrantsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.authentication_type
    import aws_sdk_athena.types.boxed_boolean


class QueryResultsS3AccessGrantsConfiguration(TypedDict, closed=True):
    enable_s3_access_grants: "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Specifies whether Amazon S3 access grants are enabled for query results.</p>"""
    create_user_level_prefix: NotRequired[
        "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>When enabled, appends the user ID as an Amazon S3 path prefix to the query result output location.</p>"""
    authentication_type: "aws_sdk_athena.types.authentication_type.AuthenticationType"
    """<p>The authentication type used for Amazon S3 access grants. Currently, only <code>DIRECTORY_IDENTITY</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultsS3AccessGrantsConfiguration) -> dict:
    out: dict = {}
    out["EnableS3AccessGrants"] = value["enable_s3_access_grants"]
    if "create_user_level_prefix" in value:
        out["CreateUserLevelPrefix"] = value["create_user_level_prefix"]
    import aws_sdk_athena.types.authentication_type

    out["AuthenticationType"] = (
        aws_sdk_athena.types.authentication_type.serialize_aws_json_1_1(
            value["authentication_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryResultsS3AccessGrantsConfiguration:
    out: QueryResultsS3AccessGrantsConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableS3AccessGrants" in data:
        out["enable_s3_access_grants"] = data["EnableS3AccessGrants"]
    else:
        raise DeserializationError(
            "QueryResultsS3AccessGrantsConfiguration.enable_s3_access_grants required"
        )
    if "CreateUserLevelPrefix" in data:
        out["create_user_level_prefix"] = data["CreateUserLevelPrefix"]
    if "AuthenticationType" in data:
        import aws_sdk_athena.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_athena.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    else:
        raise DeserializationError(
            "QueryResultsS3AccessGrantsConfiguration.authentication_type required"
        )
    return out
