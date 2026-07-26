"""Generated from Smithy shape ``com.amazonaws.acm#CertificateFilterStatement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_acm.types.certificate_filter
    import capo_acm.types.certificate_filter_statement
    import capo_acm.types.certificate_filter_statement_list


class _CertificateFilterStatement_And(TypedDict, closed=True):
    And: "capo_acm.types.certificate_filter_statement_list.CertificateFilterStatementList"


class _CertificateFilterStatement_Or(TypedDict, closed=True):
    Or: "capo_acm.types.certificate_filter_statement_list.CertificateFilterStatementList"


class _CertificateFilterStatement_Not(TypedDict, closed=True):
    Not: "capo_acm.types.certificate_filter_statement.CertificateFilterStatement"


class _CertificateFilterStatement_Filter(TypedDict, closed=True):
    Filter: "capo_acm.types.certificate_filter.CertificateFilter"


CertificateFilterStatement: TypeAlias = (
    _CertificateFilterStatement_And
    | _CertificateFilterStatement_Or
    | _CertificateFilterStatement_Not
    | _CertificateFilterStatement_Filter
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateFilterStatement) -> dict:
    if "And" in value:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "And": capo_acm.types.certificate_filter_statement_list.serialize_aws_json_1_1(
                value["And"]
            )
        }
    elif "Or" in value:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "Or": capo_acm.types.certificate_filter_statement_list.serialize_aws_json_1_1(
                value["Or"]
            )
        }
    elif "Not" in value:
        import capo_acm.types.certificate_filter_statement

        return {
            "Not": capo_acm.types.certificate_filter_statement.serialize_aws_json_1_1(
                value["Not"]
            )
        }
    elif "Filter" in value:
        import capo_acm.types.certificate_filter

        return {
            "Filter": capo_acm.types.certificate_filter.serialize_aws_json_1_1(
                value["Filter"]
            )
        }
    else:
        raise SerializationError("CertificateFilterStatement: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateFilterStatement:
    if "And" in data:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "And": capo_acm.types.certificate_filter_statement_list.deserialize_aws_json_1_1(
                data["And"]
            )
        }
    elif "Or" in data:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "Or": capo_acm.types.certificate_filter_statement_list.deserialize_aws_json_1_1(
                data["Or"]
            )
        }
    elif "Not" in data:
        import capo_acm.types.certificate_filter_statement

        return {
            "Not": capo_acm.types.certificate_filter_statement.deserialize_aws_json_1_1(
                data["Not"]
            )
        }
    elif "Filter" in data:
        import capo_acm.types.certificate_filter

        return {
            "Filter": capo_acm.types.certificate_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        }
    else:
        raise DeserializationError(
            "CertificateFilterStatement: no recognized variant key"
        )
