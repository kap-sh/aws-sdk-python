"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.db_password
    import aws_sdk_redshift_serverless.types.db_user


class GetCredentialsResponse(TypedDict, closed=True):
    db_user: NotRequired["aws_sdk_redshift_serverless.types.db_user.DbUser"]
    """<p>A database user name that is authorized to log on to the database <code>DbName</code> using the password <code>DbPassword</code>. If the specified <code>DbUser</code> exists in the database, the new user name has the same database privileges as the the user named in <code>DbUser</code>. By default, the user is added to PUBLIC.</p>"""
    db_password: NotRequired["aws_sdk_redshift_serverless.types.db_password.DbPassword"]
    """<p>A temporary password that authorizes the user name returned by <code>DbUser</code> to log on to the database <code>DbName</code>.</p>"""
    expiration: NotRequired["datetime.datetime"]
    """<p>The date and time the password in <code>DbPassword</code> expires.</p>"""
    next_refresh_time: NotRequired["datetime.datetime"]
    """<p>The date and time of when the <code>DbUser</code> and <code>DbPassword</code> authorization refreshes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCredentialsResponse) -> dict:
    out: dict = {}
    if "db_user" in value:
        out["dbUser"] = value["db_user"]
    if "db_password" in value:
        out["dbPassword"] = value["db_password"]
    if "expiration" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["expiration"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["expiration"]
            )
        )
    if "next_refresh_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["nextRefreshTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["next_refresh_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCredentialsResponse:
    out: GetCredentialsResponse = {}  # type: ignore[typeddict-item]
    if "dbUser" in data:
        out["db_user"] = data["dbUser"]
    if "dbPassword" in data:
        out["db_password"] = data["dbPassword"]
    if "expiration" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["expiration"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["expiration"]
            )
        )
    if "nextRefreshTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["next_refresh_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["nextRefreshTime"]
            )
        )
    return out
