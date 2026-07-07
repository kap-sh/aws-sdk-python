"""Generated from Smithy shape ``com.amazonaws.macie2#UserIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.assumed_role
    import aws_sdk_macie2.types.aws_account
    import aws_sdk_macie2.types.aws_service
    import aws_sdk_macie2.types.federated_user
    import aws_sdk_macie2.types.iam_user
    import aws_sdk_macie2.types.user_identity_root
    import aws_sdk_macie2.types.user_identity_type


class UserIdentity(TypedDict, closed=True):
    assumed_role: NotRequired["aws_sdk_macie2.types.assumed_role.AssumedRole"]
    """<p>If the action was performed with temporary security credentials that were obtained using the AssumeRole operation of the Security Token Service (STS) API, the identifiers, session context, and other details about the identity.</p>"""
    aws_account: NotRequired["aws_sdk_macie2.types.aws_account.AwsAccount"]
    """<p>If the action was performed using the credentials for another Amazon Web Services account, the details of that account.</p>"""
    aws_service: NotRequired["aws_sdk_macie2.types.aws_service.AwsService"]
    """<p>If the action was performed by an Amazon Web Services account that belongs to an Amazon Web Services service, the name of the service.</p>"""
    federated_user: NotRequired["aws_sdk_macie2.types.federated_user.FederatedUser"]
    """<p>If the action was performed with temporary security credentials that were obtained using the GetFederationToken operation of the Security Token Service (STS) API, the identifiers, session context, and other details about the identity.</p>"""
    iam_user: NotRequired["aws_sdk_macie2.types.iam_user.IamUser"]
    """<p>If the action was performed using the credentials for an Identity and Access Management (IAM) user, the name and other details about the user.</p>"""
    root: NotRequired["aws_sdk_macie2.types.user_identity_root.UserIdentityRoot"]
    """<p>If the action was performed using the credentials for your Amazon Web Services account, the details of your account.</p>"""
    type: NotRequired["aws_sdk_macie2.types.user_identity_type.UserIdentityType"]
    """<p>The type of entity that performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentity) -> dict:
    out: dict = {}
    if "assumed_role" in value:
        import aws_sdk_macie2.types.assumed_role

        out["assumedRole"] = aws_sdk_macie2.types.assumed_role.serialize_json(
            value["assumed_role"]
        )
    if "aws_account" in value:
        import aws_sdk_macie2.types.aws_account

        out["awsAccount"] = aws_sdk_macie2.types.aws_account.serialize_json(
            value["aws_account"]
        )
    if "aws_service" in value:
        import aws_sdk_macie2.types.aws_service

        out["awsService"] = aws_sdk_macie2.types.aws_service.serialize_json(
            value["aws_service"]
        )
    if "federated_user" in value:
        import aws_sdk_macie2.types.federated_user

        out["federatedUser"] = aws_sdk_macie2.types.federated_user.serialize_json(
            value["federated_user"]
        )
    if "iam_user" in value:
        import aws_sdk_macie2.types.iam_user

        out["iamUser"] = aws_sdk_macie2.types.iam_user.serialize_json(value["iam_user"])
    if "root" in value:
        import aws_sdk_macie2.types.user_identity_root

        out["root"] = aws_sdk_macie2.types.user_identity_root.serialize_json(
            value["root"]
        )
    if "type" in value:
        import aws_sdk_macie2.types.user_identity_type

        out["type"] = aws_sdk_macie2.types.user_identity_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> UserIdentity:
    out: UserIdentity = {}  # type: ignore[typeddict-item]
    if "assumedRole" in data:
        import aws_sdk_macie2.types.assumed_role

        out["assumed_role"] = aws_sdk_macie2.types.assumed_role.deserialize_json(
            data["assumedRole"]
        )
    if "awsAccount" in data:
        import aws_sdk_macie2.types.aws_account

        out["aws_account"] = aws_sdk_macie2.types.aws_account.deserialize_json(
            data["awsAccount"]
        )
    if "awsService" in data:
        import aws_sdk_macie2.types.aws_service

        out["aws_service"] = aws_sdk_macie2.types.aws_service.deserialize_json(
            data["awsService"]
        )
    if "federatedUser" in data:
        import aws_sdk_macie2.types.federated_user

        out["federated_user"] = aws_sdk_macie2.types.federated_user.deserialize_json(
            data["federatedUser"]
        )
    if "iamUser" in data:
        import aws_sdk_macie2.types.iam_user

        out["iam_user"] = aws_sdk_macie2.types.iam_user.deserialize_json(
            data["iamUser"]
        )
    if "root" in data:
        import aws_sdk_macie2.types.user_identity_root

        out["root"] = aws_sdk_macie2.types.user_identity_root.deserialize_json(
            data["root"]
        )
    if "type" in data:
        import aws_sdk_macie2.types.user_identity_type

        out["type"] = aws_sdk_macie2.types.user_identity_type.deserialize_json(
            data["type"]
        )
    return out
