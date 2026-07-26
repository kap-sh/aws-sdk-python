"""Generated from Smithy shape ``com.amazonaws.macie2#UserIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.assumed_role
    import capo_macie2.types.aws_account
    import capo_macie2.types.aws_service
    import capo_macie2.types.federated_user
    import capo_macie2.types.iam_user
    import capo_macie2.types.user_identity_root
    import capo_macie2.types.user_identity_type


class UserIdentity(TypedDict, closed=True):
    assumed_role: NotRequired["capo_macie2.types.assumed_role.AssumedRole"]
    """<p>If the action was performed with temporary security credentials that were obtained using the AssumeRole operation of the Security Token Service (STS) API, the identifiers, session context, and other details about the identity.</p>"""
    aws_account: NotRequired["capo_macie2.types.aws_account.AwsAccount"]
    """<p>If the action was performed using the credentials for another Amazon Web Services account, the details of that account.</p>"""
    aws_service: NotRequired["capo_macie2.types.aws_service.AwsService"]
    """<p>If the action was performed by an Amazon Web Services account that belongs to an Amazon Web Services service, the name of the service.</p>"""
    federated_user: NotRequired["capo_macie2.types.federated_user.FederatedUser"]
    """<p>If the action was performed with temporary security credentials that were obtained using the GetFederationToken operation of the Security Token Service (STS) API, the identifiers, session context, and other details about the identity.</p>"""
    iam_user: NotRequired["capo_macie2.types.iam_user.IamUser"]
    """<p>If the action was performed using the credentials for an Identity and Access Management (IAM) user, the name and other details about the user.</p>"""
    root: NotRequired["capo_macie2.types.user_identity_root.UserIdentityRoot"]
    """<p>If the action was performed using the credentials for your Amazon Web Services account, the details of your account.</p>"""
    type: NotRequired["capo_macie2.types.user_identity_type.UserIdentityType"]
    """<p>The type of entity that performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentity) -> dict:
    out: dict = {}
    if "assumed_role" in value:
        import capo_macie2.types.assumed_role

        out["assumedRole"] = capo_macie2.types.assumed_role.serialize_json(
            value["assumed_role"]
        )
    if "aws_account" in value:
        import capo_macie2.types.aws_account

        out["awsAccount"] = capo_macie2.types.aws_account.serialize_json(
            value["aws_account"]
        )
    if "aws_service" in value:
        import capo_macie2.types.aws_service

        out["awsService"] = capo_macie2.types.aws_service.serialize_json(
            value["aws_service"]
        )
    if "federated_user" in value:
        import capo_macie2.types.federated_user

        out["federatedUser"] = capo_macie2.types.federated_user.serialize_json(
            value["federated_user"]
        )
    if "iam_user" in value:
        import capo_macie2.types.iam_user

        out["iamUser"] = capo_macie2.types.iam_user.serialize_json(value["iam_user"])
    if "root" in value:
        import capo_macie2.types.user_identity_root

        out["root"] = capo_macie2.types.user_identity_root.serialize_json(value["root"])
    if "type" in value:
        import capo_macie2.types.user_identity_type

        out["type"] = capo_macie2.types.user_identity_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> UserIdentity:
    out: UserIdentity = {}  # type: ignore[typeddict-item]
    if "assumedRole" in data:
        import capo_macie2.types.assumed_role

        out["assumed_role"] = capo_macie2.types.assumed_role.deserialize_json(
            data["assumedRole"]
        )
    if "awsAccount" in data:
        import capo_macie2.types.aws_account

        out["aws_account"] = capo_macie2.types.aws_account.deserialize_json(
            data["awsAccount"]
        )
    if "awsService" in data:
        import capo_macie2.types.aws_service

        out["aws_service"] = capo_macie2.types.aws_service.deserialize_json(
            data["awsService"]
        )
    if "federatedUser" in data:
        import capo_macie2.types.federated_user

        out["federated_user"] = capo_macie2.types.federated_user.deserialize_json(
            data["federatedUser"]
        )
    if "iamUser" in data:
        import capo_macie2.types.iam_user

        out["iam_user"] = capo_macie2.types.iam_user.deserialize_json(data["iamUser"])
    if "root" in data:
        import capo_macie2.types.user_identity_root

        out["root"] = capo_macie2.types.user_identity_root.deserialize_json(
            data["root"]
        )
    if "type" in data:
        import capo_macie2.types.user_identity_type

        out["type"] = capo_macie2.types.user_identity_type.deserialize_json(
            data["type"]
        )
    return out
