"""Generated from Smithy shape ``com.amazonaws.opensearch#AuthorizedPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.principal_type
    import aws_sdk_opensearch.types.service_options
    import aws_sdk_opensearch.types.string


class AuthorizedPrincipal(TypedDict, closed=True):
    principal_type: NotRequired["aws_sdk_opensearch.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["aws_sdk_opensearch.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html\">IAM principal</a> that is allowed access to the domain.</p>"""
    service_options: NotRequired[
        "aws_sdk_opensearch.types.service_options.ServiceOptions"
    ]
    """<p>The options for the service, including the supported Regions for the endpoint access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedPrincipal) -> dict:
    out: dict = {}
    if "principal_type" in value:
        import aws_sdk_opensearch.types.principal_type

        out["PrincipalType"] = aws_sdk_opensearch.types.principal_type.serialize_json(
            value["principal_type"]
        )
    if "principal" in value:
        out["Principal"] = value["principal"]
    if "service_options" in value:
        import aws_sdk_opensearch.types.service_options

        out["ServiceOptions"] = aws_sdk_opensearch.types.service_options.serialize_json(
            value["service_options"]
        )
    return out


def deserialize_json(data: dict) -> AuthorizedPrincipal:
    out: AuthorizedPrincipal = {}  # type: ignore[typeddict-item]
    if "PrincipalType" in data:
        import aws_sdk_opensearch.types.principal_type

        out["principal_type"] = (
            aws_sdk_opensearch.types.principal_type.deserialize_json(
                data["PrincipalType"]
            )
        )
    if "Principal" in data:
        out["principal"] = data["Principal"]
    if "ServiceOptions" in data:
        import aws_sdk_opensearch.types.service_options

        out["service_options"] = (
            aws_sdk_opensearch.types.service_options.deserialize_json(
                data["ServiceOptions"]
            )
        )
    return out
