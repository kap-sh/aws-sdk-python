"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.add_header_action
    import aws_sdk_ses.types.bounce_action
    import aws_sdk_ses.types.connect_action
    import aws_sdk_ses.types.lambda_action
    import aws_sdk_ses.types.s3_action
    import aws_sdk_ses.types.sns_action
    import aws_sdk_ses.types.stop_action
    import aws_sdk_ses.types.workmail_action


class ReceiptAction(TypedDict, closed=True):
    s3_action: NotRequired["aws_sdk_ses.types.s3_action.S3Action"]
    """<p>Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.</p>"""
    bounce_action: NotRequired["aws_sdk_ses.types.bounce_action.BounceAction"]
    """<p>Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).</p>"""
    workmail_action: NotRequired["aws_sdk_ses.types.workmail_action.WorkmailAction"]
    """<p>Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.</p>"""
    lambda_action: NotRequired["aws_sdk_ses.types.lambda_action.LambdaAction"]
    """<p>Calls an Amazon Web Services Lambda function, and optionally, publishes a notification to Amazon SNS.</p>"""
    stop_action: NotRequired["aws_sdk_ses.types.stop_action.StopAction"]
    """<p>Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.</p>"""
    add_header_action: NotRequired[
        "aws_sdk_ses.types.add_header_action.AddHeaderAction"
    ]
    """<p>Adds a header to the received email.</p>"""
    sns_action: NotRequired["aws_sdk_ses.types.sns_action.SNSAction"]
    """<p>Publishes the email content within a notification to Amazon SNS.</p>"""
    connect_action: NotRequired["aws_sdk_ses.types.connect_action.ConnectAction"]
    """<p>Parses the received message and starts an email contact in Amazon Connect on your behalf.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "s3_action" in value:
        import aws_sdk_ses.types.s3_action

        aws_sdk_ses.types.s3_action.serialize_query(
            value["s3_action"], pairs, f"{prefix}.S3Action"
        )
    if "bounce_action" in value:
        import aws_sdk_ses.types.bounce_action

        aws_sdk_ses.types.bounce_action.serialize_query(
            value["bounce_action"], pairs, f"{prefix}.BounceAction"
        )
    if "workmail_action" in value:
        import aws_sdk_ses.types.workmail_action

        aws_sdk_ses.types.workmail_action.serialize_query(
            value["workmail_action"], pairs, f"{prefix}.WorkmailAction"
        )
    if "lambda_action" in value:
        import aws_sdk_ses.types.lambda_action

        aws_sdk_ses.types.lambda_action.serialize_query(
            value["lambda_action"], pairs, f"{prefix}.LambdaAction"
        )
    if "stop_action" in value:
        import aws_sdk_ses.types.stop_action

        aws_sdk_ses.types.stop_action.serialize_query(
            value["stop_action"], pairs, f"{prefix}.StopAction"
        )
    if "add_header_action" in value:
        import aws_sdk_ses.types.add_header_action

        aws_sdk_ses.types.add_header_action.serialize_query(
            value["add_header_action"], pairs, f"{prefix}.AddHeaderAction"
        )
    if "sns_action" in value:
        import aws_sdk_ses.types.sns_action

        aws_sdk_ses.types.sns_action.serialize_query(
            value["sns_action"], pairs, f"{prefix}.SNSAction"
        )
    if "connect_action" in value:
        import aws_sdk_ses.types.connect_action

        aws_sdk_ses.types.connect_action.serialize_query(
            value["connect_action"], pairs, f"{prefix}.ConnectAction"
        )


def deserialize_query(el: Element) -> ReceiptAction:
    out: ReceiptAction = {}  # type: ignore[typeddict-item]
    child_s3_action = el.find("S3Action")
    if child_s3_action is not None:
        import aws_sdk_ses.types.s3_action

        out["s3_action"] = aws_sdk_ses.types.s3_action.deserialize_query(
            child_s3_action
        )
    child_bounce_action = el.find("BounceAction")
    if child_bounce_action is not None:
        import aws_sdk_ses.types.bounce_action

        out["bounce_action"] = aws_sdk_ses.types.bounce_action.deserialize_query(
            child_bounce_action
        )
    child_workmail_action = el.find("WorkmailAction")
    if child_workmail_action is not None:
        import aws_sdk_ses.types.workmail_action

        out["workmail_action"] = aws_sdk_ses.types.workmail_action.deserialize_query(
            child_workmail_action
        )
    child_lambda_action = el.find("LambdaAction")
    if child_lambda_action is not None:
        import aws_sdk_ses.types.lambda_action

        out["lambda_action"] = aws_sdk_ses.types.lambda_action.deserialize_query(
            child_lambda_action
        )
    child_stop_action = el.find("StopAction")
    if child_stop_action is not None:
        import aws_sdk_ses.types.stop_action

        out["stop_action"] = aws_sdk_ses.types.stop_action.deserialize_query(
            child_stop_action
        )
    child_add_header_action = el.find("AddHeaderAction")
    if child_add_header_action is not None:
        import aws_sdk_ses.types.add_header_action

        out["add_header_action"] = (
            aws_sdk_ses.types.add_header_action.deserialize_query(
                child_add_header_action
            )
        )
    child_sns_action = el.find("SNSAction")
    if child_sns_action is not None:
        import aws_sdk_ses.types.sns_action

        out["sns_action"] = aws_sdk_ses.types.sns_action.deserialize_query(
            child_sns_action
        )
    child_connect_action = el.find("ConnectAction")
    if child_connect_action is not None:
        import aws_sdk_ses.types.connect_action

        out["connect_action"] = aws_sdk_ses.types.connect_action.deserialize_query(
            child_connect_action
        )
    return out
