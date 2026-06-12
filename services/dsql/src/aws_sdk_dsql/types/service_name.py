"""Generated from Smithy shape ``com.amazonaws.dsql#ServiceName``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The name of the VPC endpoint service that provides access to your cluster. Use this endpoint to establish a private connection between your VPC and the cluster.</p>"""
ServiceName: TypeAlias = str