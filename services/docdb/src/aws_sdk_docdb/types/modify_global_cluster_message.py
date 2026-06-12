"""Generated from Smithy shape ``com.amazonaws.docdb#ModifyGlobalClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.global_cluster_identifier


class ModifyGlobalClusterMessage(TypedDict):
    global_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The identifier for the global cluster being modified. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global cluster.</p> </li> </ul>"""
    new_global_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The new identifier for a global cluster when you modify a global cluster. This value is stored as a lowercase string.</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> <p>The first character must be a letter</p> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>"""
    deletion_protection: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates if the global cluster has deletion protection enabled. The global cluster can't be deleted when deletion protection is enabled. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "new_global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.NewGlobalClusterIdentifier",
                str(value["new_global_cluster_identifier"]),
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{prefix}.DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyGlobalClusterMessage:
    out: ModifyGlobalClusterMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_new_global_cluster_identifier = el.find("NewGlobalClusterIdentifier")
    if child_new_global_cluster_identifier is not None:
        out["new_global_cluster_identifier"] = str(
            child_new_global_cluster_identifier.text or ""
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    return out
