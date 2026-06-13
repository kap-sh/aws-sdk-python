"""Generated from Smithy shape ``com.amazonaws.datazone#RuleDetail``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_form_enforcement_detail
    import aws_sdk_datazone.types.glossary_term_enforcement_detail


class _RuleDetail_metadataFormEnforcementDetail(TypedDict):
    metadataFormEnforcementDetail: "aws_sdk_datazone.types.metadata_form_enforcement_detail.MetadataFormEnforcementDetail"


class _RuleDetail_glossaryTermEnforcementDetail(TypedDict):
    glossaryTermEnforcementDetail: "aws_sdk_datazone.types.glossary_term_enforcement_detail.GlossaryTermEnforcementDetail"


RuleDetail: TypeAlias = (
    _RuleDetail_metadataFormEnforcementDetail
    | _RuleDetail_glossaryTermEnforcementDetail
)


# --- restJson1 ser/de ---
def serialize_json(value: RuleDetail) -> dict:
    if "metadataFormEnforcementDetail" in value:
        import aws_sdk_datazone.types.metadata_form_enforcement_detail

        return {
            "metadataFormEnforcementDetail": aws_sdk_datazone.types.metadata_form_enforcement_detail.serialize_json(
                value["metadataFormEnforcementDetail"]
            )
        }
    elif "glossaryTermEnforcementDetail" in value:
        import aws_sdk_datazone.types.glossary_term_enforcement_detail

        return {
            "glossaryTermEnforcementDetail": aws_sdk_datazone.types.glossary_term_enforcement_detail.serialize_json(
                value["glossaryTermEnforcementDetail"]
            )
        }
    else:
        raise SerializationError("RuleDetail: no variant present")


def deserialize_json(data: dict) -> RuleDetail:
    if "metadataFormEnforcementDetail" in data:
        import aws_sdk_datazone.types.metadata_form_enforcement_detail

        return {
            "metadataFormEnforcementDetail": aws_sdk_datazone.types.metadata_form_enforcement_detail.deserialize_json(
                data["metadataFormEnforcementDetail"]
            )
        }
    elif "glossaryTermEnforcementDetail" in data:
        import aws_sdk_datazone.types.glossary_term_enforcement_detail

        return {
            "glossaryTermEnforcementDetail": aws_sdk_datazone.types.glossary_term_enforcement_detail.deserialize_json(
                data["glossaryTermEnforcementDetail"]
            )
        }
    else:
        raise DeserializationError("RuleDetail: no recognized variant key")
