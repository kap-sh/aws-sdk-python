"""Generated from Smithy shape ``com.amazonaws.securityagent#Assets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.actor_list
    import aws_sdk_securityagent.types.document_list
    import aws_sdk_securityagent.types.endpoint_list
    import aws_sdk_securityagent.types.integrated_repository_list
    import aws_sdk_securityagent.types.source_code_repository_list


class Assets(TypedDict, closed=True):
    endpoints: NotRequired["aws_sdk_securityagent.types.endpoint_list.EndpointList"]
    """<p>The list of endpoints to test during the pentest.</p>"""
    actors: NotRequired["aws_sdk_securityagent.types.actor_list.ActorList"]
    """<p>The list of actors used during penetration testing.</p>"""
    documents: NotRequired["aws_sdk_securityagent.types.document_list.DocumentList"]
    """<p>The list of documents that provide context for the pentest.</p>"""
    source_code: NotRequired[
        "aws_sdk_securityagent.types.source_code_repository_list.SourceCodeRepositoryList"
    ]
    """<p>The list of source code repositories to analyze during the pentest.</p>"""
    integrated_repositories: NotRequired[
        "aws_sdk_securityagent.types.integrated_repository_list.IntegratedRepositoryList"
    ]
    """<p>The list of integrated repositories associated with the pentest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Assets) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_securityagent.types.endpoint_list

        out["endpoints"] = aws_sdk_securityagent.types.endpoint_list.serialize_json(
            value["endpoints"]
        )
    if "actors" in value:
        import aws_sdk_securityagent.types.actor_list

        out["actors"] = aws_sdk_securityagent.types.actor_list.serialize_json(
            value["actors"]
        )
    if "documents" in value:
        import aws_sdk_securityagent.types.document_list

        out["documents"] = aws_sdk_securityagent.types.document_list.serialize_json(
            value["documents"]
        )
    if "source_code" in value:
        import aws_sdk_securityagent.types.source_code_repository_list

        out["sourceCode"] = (
            aws_sdk_securityagent.types.source_code_repository_list.serialize_json(
                value["source_code"]
            )
        )
    if "integrated_repositories" in value:
        import aws_sdk_securityagent.types.integrated_repository_list

        out["integratedRepositories"] = (
            aws_sdk_securityagent.types.integrated_repository_list.serialize_json(
                value["integrated_repositories"]
            )
        )
    return out


def deserialize_json(data: dict) -> Assets:
    out: Assets = {}  # type: ignore[typeddict-item]
    if "endpoints" in data:
        import aws_sdk_securityagent.types.endpoint_list

        out["endpoints"] = aws_sdk_securityagent.types.endpoint_list.deserialize_json(
            data["endpoints"]
        )
    if "actors" in data:
        import aws_sdk_securityagent.types.actor_list

        out["actors"] = aws_sdk_securityagent.types.actor_list.deserialize_json(
            data["actors"]
        )
    if "documents" in data:
        import aws_sdk_securityagent.types.document_list

        out["documents"] = aws_sdk_securityagent.types.document_list.deserialize_json(
            data["documents"]
        )
    if "sourceCode" in data:
        import aws_sdk_securityagent.types.source_code_repository_list

        out["source_code"] = (
            aws_sdk_securityagent.types.source_code_repository_list.deserialize_json(
                data["sourceCode"]
            )
        )
    if "integratedRepositories" in data:
        import aws_sdk_securityagent.types.integrated_repository_list

        out["integrated_repositories"] = (
            aws_sdk_securityagent.types.integrated_repository_list.deserialize_json(
                data["integratedRepositories"]
            )
        )
    return out
