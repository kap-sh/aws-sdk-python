"""Generated from Smithy shape ``com.amazonaws.securityhub#Criteria``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ocsf_finding_filters


class _Criteria_OcsfFindingCriteria(TypedDict):
    OcsfFindingCriteria: (
        "aws_sdk_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
    )


Criteria: TypeAlias = _Criteria_OcsfFindingCriteria


# --- restJson1 ser/de ---
def serialize_json(value: Criteria) -> dict:
    if "OcsfFindingCriteria" in value:
        import aws_sdk_securityhub.types.ocsf_finding_filters

        return {
            "OcsfFindingCriteria": aws_sdk_securityhub.types.ocsf_finding_filters.serialize_json(
                value["OcsfFindingCriteria"]
            )
        }
    else:
        raise SerializationError("Criteria: no variant present")


def deserialize_json(data: dict) -> Criteria:
    if "OcsfFindingCriteria" in data:
        import aws_sdk_securityhub.types.ocsf_finding_filters

        return {
            "OcsfFindingCriteria": aws_sdk_securityhub.types.ocsf_finding_filters.deserialize_json(
                data["OcsfFindingCriteria"]
            )
        }
    else:
        raise DeserializationError("Criteria: no recognized variant key")
