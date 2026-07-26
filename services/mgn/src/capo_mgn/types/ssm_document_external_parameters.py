"""Generated from Smithy shape ``com.amazonaws.mgn#SsmDocumentExternalParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.ssm_document_parameter_name
    import capo_mgn.types.ssm_external_parameter

SsmDocumentExternalParameters: TypeAlias = dict[
    "capo_mgn.types.ssm_document_parameter_name.SsmDocumentParameterName",
    "capo_mgn.types.ssm_external_parameter.SsmExternalParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SsmDocumentExternalParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_mgn.types.ssm_external_parameter

        out[key] = capo_mgn.types.ssm_external_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SsmDocumentExternalParameters:
    out: SsmDocumentExternalParameters = {}
    for key, value in data.items():
        import capo_mgn.types.ssm_external_parameter

        out[key] = capo_mgn.types.ssm_external_parameter.deserialize_json(value)
    return out
