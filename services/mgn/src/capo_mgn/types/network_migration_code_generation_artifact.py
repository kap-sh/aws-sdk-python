"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.checksum
    import capo_mgn.types.logical_id
    import capo_mgn.types.network_migration_code_generation_artifact_id
    import capo_mgn.types.network_migration_code_generation_artifact_sub_type
    import capo_mgn.types.network_migration_code_generation_artifact_type
    import capo_mgn.types.s3_configuration


class NetworkMigrationCodeGenerationArtifact(TypedDict, closed=True):
    artifact_id: NotRequired[
        "capo_mgn.types.network_migration_code_generation_artifact_id.NetworkMigrationCodeGenerationArtifactID"
    ]
    """<p>The unique identifier of the artifact.</p>"""
    artifact_type: NotRequired[
        "capo_mgn.types.network_migration_code_generation_artifact_type.NetworkMigrationCodeGenerationArtifactType"
    ]
    """<p>The type of the artifact, such as CLOUDFORMATION_TEMPLATE or TERRAFORM_MODULE.</p>"""
    artifact_sub_type: NotRequired[
        "capo_mgn.types.network_migration_code_generation_artifact_sub_type.NetworkMigrationCodeGenerationArtifactSubType"
    ]
    """<p>The sub-type of the artifact for further classification.</p>"""
    logical_id: NotRequired["capo_mgn.types.logical_id.LogicalID"]
    """<p>The logical identifier for the artifact.</p>"""
    output_s3_configuration: NotRequired[
        "capo_mgn.types.s3_configuration.S3Configuration"
    ]
    """<p>The S3 location where the artifact is stored.</p>"""
    checksum: NotRequired["capo_mgn.types.checksum.Checksum"]
    """<p>The checksum of the artifact for integrity verification.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the artifact was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationArtifact) -> dict:
    out: dict = {}
    if "artifact_id" in value:
        out["artifactID"] = value["artifact_id"]
    if "artifact_type" in value:
        out["artifactType"] = value["artifact_type"]
    if "artifact_sub_type" in value:
        out["artifactSubType"] = value["artifact_sub_type"]
    if "logical_id" in value:
        out["logicalID"] = value["logical_id"]
    if "output_s3_configuration" in value:
        import capo_mgn.types.s3_configuration

        out["outputS3Configuration"] = capo_mgn.types.s3_configuration.serialize_json(
            value["output_s3_configuration"]
        )
    if "checksum" in value:
        import capo_mgn.types.checksum

        out["checksum"] = capo_mgn.types.checksum.serialize_json(value["checksum"])
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationCodeGenerationArtifact:
    out: NetworkMigrationCodeGenerationArtifact = {}  # type: ignore[typeddict-item]
    if "artifactID" in data:
        out["artifact_id"] = data["artifactID"]
    if "artifactType" in data:
        out["artifact_type"] = data["artifactType"]
    if "artifactSubType" in data:
        out["artifact_sub_type"] = data["artifactSubType"]
    if "logicalID" in data:
        out["logical_id"] = data["logicalID"]
    if "outputS3Configuration" in data:
        import capo_mgn.types.s3_configuration

        out["output_s3_configuration"] = (
            capo_mgn.types.s3_configuration.deserialize_json(
                data["outputS3Configuration"]
            )
        )
    if "checksum" in data:
        import capo_mgn.types.checksum

        out["checksum"] = capo_mgn.types.checksum.deserialize_json(data["checksum"])
    if "createdAt" in data:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
