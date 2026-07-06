"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.sensitive_string
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class ClusterCredentials(TypedDict, closed=True):
    db_user: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A database user name that is authorized to log on to the database <code>DbName</code> using the password <code>DbPassword</code>. If the specified DbUser exists in the database, the new user name has the same database permissions as the the user named in DbUser. By default, the user is added to PUBLIC. If the <code>DbGroups</code> parameter is specifed, <code>DbUser</code> is added to the listed groups for any sessions created using these credentials.</p>"""
    db_password: NotRequired["aws_sdk_redshift.types.sensitive_string.SensitiveString"]
    """<p>A temporary password that authorizes the user name returned by <code>DbUser</code> to log on to the database <code>DbName</code>. </p>"""
    expiration: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date and time the password in <code>DbPassword</code> expires.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterCredentials, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_user" in value:
        pairs.append((f"{prefix}.DbUser", str(value["db_user"])))
    if "db_password" in value:
        pairs.append((f"{prefix}.DbPassword", str(value["db_password"])))
    if "expiration" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["expiration"], pairs, f"{prefix}.Expiration"
        )


def deserialize_query(el: Element) -> ClusterCredentials:
    out: ClusterCredentials = {}  # type: ignore[typeddict-item]
    child_db_user = el.find("DbUser")
    if child_db_user is not None:
        out["db_user"] = str(child_db_user.text or "")
    child_db_password = el.find("DbPassword")
    if child_db_password is not None:
        out["db_password"] = str(child_db_password.text or "")
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import aws_sdk_redshift.types.t_stamp

        out["expiration"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_expiration
        )
    return out
