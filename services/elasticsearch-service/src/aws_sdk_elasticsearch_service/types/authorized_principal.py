"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AuthorizedPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.principal_type
    import aws_sdk_elasticsearch_service.types.string


class AuthorizedPrincipal(TypedDict, closed=True):
    principal_type: NotRequired[
        "aws_sdk_elasticsearch_service.types.principal_type.PrincipalType"
    ]
    """<p>The type of principal.</p>"""
    principal: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The IAM principal that is allowed access to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedPrincipal) -> dict:
    out: dict = {}
    if "principal_type" in value:
        import aws_sdk_elasticsearch_service.types.principal_type

        out["PrincipalType"] = (
            aws_sdk_elasticsearch_service.types.principal_type.serialize_json(
                value["principal_type"]
            )
        )
    if "principal" in value:
        out["Principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> AuthorizedPrincipal:
    out: AuthorizedPrincipal = {}  # type: ignore[typeddict-item]
    if "PrincipalType" in data:
        import aws_sdk_elasticsearch_service.types.principal_type

        out["principal_type"] = (
            aws_sdk_elasticsearch_service.types.principal_type.deserialize_json(
                data["PrincipalType"]
            )
        )
    if "Principal" in data:
        out["principal"] = data["Principal"]
    return out
