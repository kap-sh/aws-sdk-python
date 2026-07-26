"""Generated from Smithy shape ``com.amazonaws.bedrock#ImportedModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.imported_model_arn
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.instruct_supported
    import capo_bedrock.types.model_architecture
    import capo_bedrock.types.timestamp


class ImportedModelSummary(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.imported_model_arn.ImportedModelArn"
    """<p>The Amazon Resource Name (ARN) of the imported model.</p>"""
    model_name: "capo_bedrock.types.imported_model_name.ImportedModelName"
    """<p>Name of the imported model.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>Creation time of the imported model.</p>"""
    instruct_supported: NotRequired[
        "capo_bedrock.types.instruct_supported.InstructSupported"
    ]
    """<p>Specifies if the imported model supports converse.</p>"""
    model_architecture: NotRequired[
        "capo_bedrock.types.model_architecture.ModelArchitecture"
    ]
    """<p>The architecture of the imported model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportedModelSummary) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    out["modelName"] = value["model_name"]
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "instruct_supported" in value:
        out["instructSupported"] = value["instruct_supported"]
    if "model_architecture" in value:
        out["modelArchitecture"] = value["model_architecture"]
    return out


def deserialize_json(data: dict) -> ImportedModelSummary:
    out: ImportedModelSummary = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("ImportedModelSummary.model_arn required")
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    else:
        raise DeserializationError("ImportedModelSummary.model_name required")
    if "creationTime" in data:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ImportedModelSummary.creation_time required")
    if "instructSupported" in data:
        out["instruct_supported"] = data["instructSupported"]
    if "modelArchitecture" in data:
        out["model_architecture"] = data["modelArchitecture"]
    return out
