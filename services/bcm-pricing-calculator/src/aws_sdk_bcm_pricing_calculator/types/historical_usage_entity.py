"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#HistoricalUsageEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.account_id
    import aws_sdk_bcm_pricing_calculator.types.bill_interval
    import aws_sdk_bcm_pricing_calculator.types.expression
    import aws_sdk_bcm_pricing_calculator.types.operation
    import aws_sdk_bcm_pricing_calculator.types.service_code
    import aws_sdk_bcm_pricing_calculator.types.usage_type


class HistoricalUsageEntity(TypedDict):
    service_code: "aws_sdk_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code associated with the usage. </p>"""
    usage_type: "aws_sdk_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage. </p>"""
    operation: "aws_sdk_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with the usage. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with the usage. </p>"""
    usage_account_id: "aws_sdk_bcm_pricing_calculator.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID associated with the usage. </p>"""
    bill_interval: "aws_sdk_bcm_pricing_calculator.types.bill_interval.BillInterval"
    """<p> The time interval for the historical usage data. </p>"""
    filter_expression: "aws_sdk_bcm_pricing_calculator.types.expression.Expression"
    """<p> An optional filter expression to apply to the historical usage data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoricalUsageEntity) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "location" in value:
        out["location"] = value["location"]
    out["usageAccountId"] = value["usage_account_id"]
    import aws_sdk_bcm_pricing_calculator.types.bill_interval

    out["billInterval"] = (
        aws_sdk_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
            value["bill_interval"]
        )
    )
    import aws_sdk_bcm_pricing_calculator.types.expression

    out["filterExpression"] = (
        aws_sdk_bcm_pricing_calculator.types.expression.serialize_aws_json_1_0(
            value["filter_expression"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> HistoricalUsageEntity:
    out: HistoricalUsageEntity = {}  # type: ignore[typeddict-item]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError("HistoricalUsageEntity.service_code required")
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    else:
        raise DeserializationError("HistoricalUsageEntity.usage_type required")
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError("HistoricalUsageEntity.operation required")
    if "location" in data:
        out["location"] = data["location"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    else:
        raise DeserializationError("HistoricalUsageEntity.usage_account_id required")
    if "billInterval" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    else:
        raise DeserializationError("HistoricalUsageEntity.bill_interval required")
    if "filterExpression" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression

        out["filter_expression"] = (
            aws_sdk_bcm_pricing_calculator.types.expression.deserialize_aws_json_1_0(
                data["filterExpression"]
            )
        )
    else:
        raise DeserializationError("HistoricalUsageEntity.filter_expression required")
    return out
