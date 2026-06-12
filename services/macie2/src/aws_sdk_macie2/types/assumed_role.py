"""Generated from Smithy shape ``com.amazonaws.macie2#AssumedRole``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.session_context


class AssumedRole(TypedDict):
    access_key_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services access key ID that identifies the credentials.</p>"""
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that owns the entity that was used to get the credentials.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the entity that was used to get the credentials.</p>"""
    principal_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the entity that was used to get the credentials.</p>"""
    session_context: NotRequired["aws_sdk_macie2.types.session_context.SessionContext"]
    """<p>The details of the session that was created for the credentials, including the entity that issued the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumedRole) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "session_context" in value:
        import aws_sdk_macie2.types.session_context

        out["sessionContext"] = aws_sdk_macie2.types.session_context.serialize_json(
            value["session_context"]
        )
    return out


def deserialize_json(data: dict) -> AssumedRole:
    out: AssumedRole = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    if "sessionContext" in data:
        import aws_sdk_macie2.types.session_context

        out["session_context"] = aws_sdk_macie2.types.session_context.deserialize_json(
            data["sessionContext"]
        )
    return out
