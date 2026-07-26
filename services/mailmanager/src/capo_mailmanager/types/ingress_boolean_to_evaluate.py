"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressBooleanToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_analysis
    import capo_mailmanager.types.ingress_is_in_address_list


class _IngressBooleanToEvaluate_Analysis(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.ingress_analysis.IngressAnalysis"


class _IngressBooleanToEvaluate_IsInAddressList(TypedDict, closed=True):
    IsInAddressList: (
        "capo_mailmanager.types.ingress_is_in_address_list.IngressIsInAddressList"
    )


IngressBooleanToEvaluate: TypeAlias = (
    _IngressBooleanToEvaluate_Analysis | _IngressBooleanToEvaluate_IsInAddressList
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressBooleanToEvaluate) -> dict:
    if "Analysis" in value:
        import capo_mailmanager.types.ingress_analysis

        return {
            "Analysis": capo_mailmanager.types.ingress_analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    elif "IsInAddressList" in value:
        import capo_mailmanager.types.ingress_is_in_address_list

        return {
            "IsInAddressList": capo_mailmanager.types.ingress_is_in_address_list.serialize_aws_json_1_0(
                value["IsInAddressList"]
            )
        }
    else:
        raise SerializationError("IngressBooleanToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressBooleanToEvaluate:
    if "Analysis" in data:
        import capo_mailmanager.types.ingress_analysis

        return {
            "Analysis": capo_mailmanager.types.ingress_analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    elif "IsInAddressList" in data:
        import capo_mailmanager.types.ingress_is_in_address_list

        return {
            "IsInAddressList": capo_mailmanager.types.ingress_is_in_address_list.deserialize_aws_json_1_0(
                data["IsInAddressList"]
            )
        }
    else:
        raise DeserializationError(
            "IngressBooleanToEvaluate: no recognized variant key"
        )
