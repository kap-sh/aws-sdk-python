"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventPerformedBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.iam_principal_arn
    import capo_connectcases.types.user_union


class AuditEventPerformedBy(TypedDict, closed=True):
    user: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    iam_principal_arn: "capo_connectcases.types.iam_principal_arn.IamPrincipalArn"
    """<p>Unique identifier of an IAM role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventPerformedBy) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_connectcases.types.user_union

        out["user"] = capo_connectcases.types.user_union.serialize_json(value["user"])
    out["iamPrincipalArn"] = value["iam_principal_arn"]
    return out


def deserialize_json(data: dict) -> AuditEventPerformedBy:
    out: AuditEventPerformedBy = {}  # type: ignore[typeddict-item]
    if "user" in data:
        import capo_connectcases.types.user_union

        out["user"] = capo_connectcases.types.user_union.deserialize_json(data["user"])
    if "iamPrincipalArn" in data:
        out["iam_principal_arn"] = data["iamPrincipalArn"]
    else:
        raise DeserializationError("AuditEventPerformedBy.iam_principal_arn required")
    return out
