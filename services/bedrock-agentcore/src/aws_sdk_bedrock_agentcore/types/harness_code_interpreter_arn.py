"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessCodeInterpreterArn``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""Code Interpreter ARN for Harness tool configuration. Accepts both managed (aws.codeinterpreter.v1) and custom code interpreter ARNs."""
HarnessCodeInterpreterArn: TypeAlias = str