"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Principal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.principal_arn
    import aws_sdk_service_catalog.types.principal_type


class Principal(TypedDict):
    principal_arn: NotRequired[
        "aws_sdk_service_catalog.types.principal_arn.PrincipalARN"
    ]
    r"""<p>The ARN of the principal (user, role, or group). This field allows for an ARN with no <code>accountID</code>, with or without wildcard characters if the <code>PrincipalType</code> is an <code>IAM_PATTERN</code>. </p> <p>For more information, review <a href=\"https://docs.aws.amazon.com/cli/latest/reference/servicecatalog/associate-principal-with-portfolio.html#options\">associate-principal-with-portfolio</a> in the Amazon Web Services CLI Command Reference. </p>"""
    principal_type: NotRequired[
        "aws_sdk_service_catalog.types.principal_type.PrincipalType"
    ]
    """<p>The principal type. The supported value is <code>IAM</code> if you use a fully defined ARN, or <code>IAM_PATTERN</code> if you use an ARN with no <code>accountID</code>, with or without wildcard characters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Principal) -> dict:
    out: dict = {}
    if "principal_arn" in value:
        out["PrincipalARN"] = value["principal_arn"]
    if "principal_type" in value:
        import aws_sdk_service_catalog.types.principal_type

        out["PrincipalType"] = (
            aws_sdk_service_catalog.types.principal_type.serialize_aws_json_1_1(
                value["principal_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Principal:
    out: Principal = {}  # type: ignore[typeddict-item]
    if "PrincipalARN" in data:
        out["principal_arn"] = data["PrincipalARN"]
    if "PrincipalType" in data:
        import aws_sdk_service_catalog.types.principal_type

        out["principal_type"] = (
            aws_sdk_service_catalog.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    return out
