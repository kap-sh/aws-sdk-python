"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Identity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.group_identity
    import capo_iotsitewise.types.iam_role_identity
    import capo_iotsitewise.types.iam_user_identity
    import capo_iotsitewise.types.user_identity


class Identity(TypedDict, closed=True):
    user: NotRequired["capo_iotsitewise.types.user_identity.UserIdentity"]
    """<p>An IAM Identity Center user identity.</p>"""
    group: NotRequired["capo_iotsitewise.types.group_identity.GroupIdentity"]
    """<p>An IAM Identity Center group identity.</p>"""
    iam_user: NotRequired["capo_iotsitewise.types.iam_user_identity.IAMUserIdentity"]
    """<p>An IAM user identity.</p>"""
    iam_role: NotRequired["capo_iotsitewise.types.iam_role_identity.IAMRoleIdentity"]
    """<p>An IAM role identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Identity) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_iotsitewise.types.user_identity

        out["user"] = capo_iotsitewise.types.user_identity.serialize_json(value["user"])
    if "group" in value:
        import capo_iotsitewise.types.group_identity

        out["group"] = capo_iotsitewise.types.group_identity.serialize_json(
            value["group"]
        )
    if "iam_user" in value:
        import capo_iotsitewise.types.iam_user_identity

        out["iamUser"] = capo_iotsitewise.types.iam_user_identity.serialize_json(
            value["iam_user"]
        )
    if "iam_role" in value:
        import capo_iotsitewise.types.iam_role_identity

        out["iamRole"] = capo_iotsitewise.types.iam_role_identity.serialize_json(
            value["iam_role"]
        )
    return out


def deserialize_json(data: dict) -> Identity:
    out: Identity = {}  # type: ignore[typeddict-item]
    if "user" in data:
        import capo_iotsitewise.types.user_identity

        out["user"] = capo_iotsitewise.types.user_identity.deserialize_json(
            data["user"]
        )
    if "group" in data:
        import capo_iotsitewise.types.group_identity

        out["group"] = capo_iotsitewise.types.group_identity.deserialize_json(
            data["group"]
        )
    if "iamUser" in data:
        import capo_iotsitewise.types.iam_user_identity

        out["iam_user"] = capo_iotsitewise.types.iam_user_identity.deserialize_json(
            data["iamUser"]
        )
    if "iamRole" in data:
        import capo_iotsitewise.types.iam_role_identity

        out["iam_role"] = capo_iotsitewise.types.iam_role_identity.deserialize_json(
            data["iamRole"]
        )
    return out
